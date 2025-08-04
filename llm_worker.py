# llm_worker.py
import multiprocessing
import time
from LLM import LLM
import whisper

def run_llm_worker(llm_job_queue):
    print("[LLM Worker] Started, loading LLM...")
    llm = None
    model_path = None
    while True:
        job = llm_job_queue.get()  # This will block until a job arrives
        if job is None:
            print("[LLM Worker] Received shutdown signal. Exiting.")
            break
        print(f"[LLM Worker] Got job: {job}")
        audio_path = job.get("audio_path")
        save_dir = job.get("save_dir")
        llm_model_path = job.get("llm_model_path", "TomoBrain/Models/Phi-3-mini-4k-instruct-q4.gguf")

        # Only reload LLM if the path changed
        if llm is None or model_path != llm_model_path:
            llm = LLM(model_path=llm_model_path)
            model_path = llm_model_path

        # Transcribe
        print("[LLM Worker] Transcribing audio with Whisper...")
        whisper_model = whisper.load_model("tiny")
        result = whisper_model.transcribe(audio_path)
        transcript = result["text"].encode('utf-8', errors='replace').decode('utf-8', errors='replace')
        print("[LLM Worker] Transcript:", transcript)
        if save_dir:
            with open(f"{save_dir}/transcript.txt", "w", encoding="utf-8") as f:
                f.write(transcript)

        # Run LLM logic
        llmRec = llm.query_llama_streaming_journal(transcript, save_dir=save_dir)
        llm.query_llama_streaming_recommendation(llmRec, save_dir=save_dir)
        if save_dir:
            with open(f"{save_dir}/done.txt", "w") as f:
                f.write("done")

        print("[LLM Worker] Job complete.\n")

# Optional: If you want to run the worker from this file
if __name__ == "__main__":
    import multiprocessing
    llm_job_queue = multiprocessing.Queue()
    run_llm_worker(llm_job_queue)
