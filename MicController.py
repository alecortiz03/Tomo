import os
import sounddevice as sd
import numpy as np
import wave
from queue import Queue
from datetime import datetime
import json

SAMPLE_RATE = 16000  # Or whatever sample rate you're using

q = Queue()

class MicController:
    def __init__(self, llm_job_queue=None):
        self.stream = None
        self.running = False
        self.recording_stream = None
        self.recording = False
        self.recorded_frames = []
        self.llm_job_queue = llm_job_queue  # <<-- NEW

    def start(self):
        if not self.running:
            self.stream = sd.RawInputStream(
                samplerate=SAMPLE_RATE,
                blocksize=8000,
                dtype='int16',
                channels=1,
                callback=self.callback
            )
            self.stream.start()
            self.running = True

    def stop(self):
        if self.stream and self.running:
            self.stream.stop()
            self.stream.close()
            self.running = False

    def callback(self, indata, frames, time, status):
        if status:
            print(status)
        q.put(bytes(indata))

    def start_recording(self):
        """Start recording audio and store it in memory until stopped."""
        if not self.recording:
            print("[INFO] Recording started.")
            self.recorded_frames = []
            self.recording_stream = sd.InputStream(
                samplerate=SAMPLE_RATE,
                channels=1,
                dtype='int16',
                callback=self.record_callback
            )
            self.recording_stream.start()
            self.recording = True

    def record_callback(self, indata, frames, time, status):
        if status:
            print("[Recording Status]", status)
        # Store audio frames as bytes
        self.recorded_frames.append(indata.copy())

    def stop_recording(self, ui, save_dir=None, progress_label=None, llm_model_path=None):
        """
        Stop recording, save the audio as a .wav file, and send a job to the LLM worker queue.
        """
        if self.recording_stream and self.recording:
            self.recording_stream.stop()
            self.recording_stream.close()
            self.recording = False
            print("[INFO] Recording stopped.")

            # Save audio to current user's folder
            user_json = "TomoBrain/Data/Users/current_user.json"
            username = "unknown"
            if os.path.exists(user_json):
                with open(user_json) as f:
                    try:
                        user_data = json.load(f)
                        username = user_data.get("username", "unknown")
                    except Exception as e:
                        print(f"Error loading user: {e}")
            if save_dir is not None:
                os.makedirs(save_dir, exist_ok=True)
                out_path = os.path.join(save_dir, "audio.wav")
            else:
                folder = f"TomoBrain/Data/Users/{username}/Recordings"
                os.makedirs(folder, exist_ok=True)
                timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                out_path = os.path.join(folder, f"recording_{timestamp}.wav")

            # Combine frames and save as .wav
            audio = np.concatenate(self.recorded_frames, axis=0)
            with wave.open(out_path, 'wb') as wf:
                wf.setnchannels(1)
                wf.setsampwidth(2)  # 'int16' == 2 bytes
                wf.setframerate(SAMPLE_RATE)
                wf.writeframes(audio.tobytes())
            print(f"[INFO] Recording saved to {out_path}")

            # --- Put job in LLM queue ---
            if self.llm_job_queue is not None:
                job = {
                    "audio_path": out_path,
                    "save_dir": save_dir,
                    "llm_model_path": llm_model_path,
                }
                print(f"[INFO] Sending job to LLM worker: {job}")
                self.llm_job_queue.put(job)
            else:
                print("[WARN] No llm_job_queue specified, skipping LLM worker.")

