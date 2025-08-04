# This Python file uses the following encoding: utf-8
import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import QTimer
from PySide6.QtGui import QMovie
from PySide6.QtWidgets import QScroller
from LoginHelper import loginSubmit, registerSubmit, checkLogin, logout
from mainMenu import notification
from NotificationManager import checkNotification
from results import load_all_dsm_graphs, load_notes
from MicController import MicController
from ui_form import Ui_MainWindow
from resources import load_resources
from session import run_grounding_session, boxBreathing
from watch import store_paired_watch_mac_from_ui
import multiprocessing
from llm_worker import run_llm_worker
import socket
from heartRate import getHeartRate

import threading
import serial
import re
import json

def background_serial_heart_rate_listener():
    PORT = '/dev/ttyUSB0'
    BAUD = 115200
    last_mac_address = None

    try:
        ser = serial.Serial(PORT, BAUD, timeout=1)
        print(f"[SERIAL] Opened {PORT} at {BAUD} baud.")
        import time
        time.sleep(2)

        while True:
            if ser.in_waiting:
                line = ser.readline().decode(errors='ignore').strip()
                mac_match = re.match(r'^Received from MAC:\s*([0-9A-Fa-f:]{17})$', line)
                if mac_match:
                    last_mac_address = mac_match.group(1).upper()
                    print(f"[SERIAL] Received from MAC: {last_mac_address}")
                elif re.fullmatch(r'(\d+\s*,\s*)*\d+', line):
                    numbers = [int(n.strip()) for n in line.split(',')]
                    print("[SERIAL] Numbers:", numbers)
                    if last_mac_address:
                        paired_json_path = os.path.join("TomoBrain", "Data", "pairedWatches.json")
                        if os.path.exists(paired_json_path):
                            with open(paired_json_path, "r") as f:
                                try:
                                    paired_dict = json.load(f)
                                except Exception:
                                    paired_dict = {}
                            user = paired_dict.get(last_mac_address)
                            if user:
                                heart_rate_folder = os.path.join("TomoBrain", "Data", "Users", user, "HeartRateStats")
                                os.makedirs(heart_rate_folder, exist_ok=True)
                                heart_rate_path = os.path.join(heart_rate_folder, "heartRate.json")
                                if os.path.exists(heart_rate_path):
                                    try:
                                        with open(heart_rate_path, "r") as f:
                                            heart_rate_data = json.load(f)
                                    except Exception:
                                        heart_rate_data = []
                                else:
                                    heart_rate_data = []
                                heart_rate_data.extend(numbers)
                                with open(heart_rate_path, "w") as f:
                                    json.dump(heart_rate_data, f, indent=2)
                                print(f"[SERIAL] Updated {heart_rate_path} with {numbers}")
                            else:
                                print(f"[SERIAL][WARN] MAC {last_mac_address} not paired to a user!")
                        else:
                            print("[SERIAL][WARN] pairedWatches.json not found!")
                    else:
                        print("[SERIAL][WARN] No MAC address received before numbers; ignoring.")
                # else: print(line)  # Optionally print other lines for debug
            else:
                import time
                time.sleep(0.1)
    except Exception as e:
        print(f"[SERIAL][ERROR] {e}")
    finally:
        try:
            ser.close()
        except:
            pass
        print("[SERIAL] Serial port closed.")




class MainWindow(QMainWindow):
    def __init__(self, llm_job_queue, llm_worker_process, parent=None):  # <-- now receives both
        super().__init__(parent)
        self.llm_job_queue = llm_job_queue
        self.llm_worker_process = llm_worker_process  # <-- store reference
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.tomoFaceAnimation = QMovie("Assets/TomoFace.gif")
        self.tomoFaceAnimation.setSpeed(100)
        self.ui.tomoFace.setMovie(self.tomoFaceAnimation)
        self.mic = MicController(llm_job_queue=self.llm_job_queue)

        if checkLogin():
            self.notificationCheck()
            self.ui.stackedWidget.setCurrentWidget(self.ui.Dashboard)
            self.tomoFaceAnimation.start()
        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.entryScreen)

        self.notif_timer = QTimer()
        self.notif_timer.timeout.connect(self.notificationCheck)
        self.notif_timer.start(1000)
        # === Entry Screen ===
        self.ui.registerButton.clicked.connect(self.goToRegister)
        self.ui.loginButton.clicked.connect(self.goToLogin)
        self.ui.backButtonRegister.clicked.connect(self.goToEntry)
        self.ui.submitButtonRegister.clicked.connect(self.submitAccount)
        self.ui.loginSubmitButton.clicked.connect(self.submitLogin)
        self.ui.powerOffButtonLogin.clicked.connect(self.powerOff)
        self.ui.backButtonLogin.clicked.connect(self.goToEntry)
        self.ui.powerOffButton.clicked.connect(self.powerOff)
        # === Dashboard ===
        self.ui.powerOffButtonDashboard.clicked.connect(self.powerOff)
        self.ui.notificationButton.clicked.connect(self.notification)
        self.ui.logoffButton.clicked.connect(self.signout)
        self.ui.resultsButton.clicked.connect(self.goToResults)
        self.ui.sampleButton.clicked.connect(self.goToSample)
        self.ui.pairWatchButton.clicked.connect(self.goToPairWatch)
        self.ui.heartRateButton.clicked.connect(self.goToHeartRate)
        # === Notifications ===
        self.ui.powerOffButtonNotificationPage.clicked.connect(self.powerOff)
        self.ui.homeButtonNotificationPage.clicked.connect(self.goToDashboard)
        self.ui.resultsButtonNotificationPage.clicked.connect(self.goToResults)
        QScroller.grabGesture(self.ui.notificationsScrollArea.viewport(), QScroller.LeftMouseButtonGesture)
        # === Results Page ===
        self.ui.homeButtonResultsPage.clicked.connect(self.goToDashboard)
        self.ui.notificationButtonResults.clicked.connect(self.notification)
        QScroller.grabGesture(self.ui.notesScrollArea.viewport(), QScroller.LeftMouseButtonGesture)
        QScroller.grabGesture(self.ui.resultsScrollArea.viewport(), QScroller.LeftMouseButtonGesture)
        QScroller.grabGesture(self.ui.resourcesScrollArea.viewport(), QScroller.LeftMouseButtonGesture)

        load_notes(self.ui, self.mic)
        self.ui.journalTextBack.clicked.connect(self.goToResults)
        self.ui.backJournalRecomButton.clicked.connect(self.goToResults)
        # === Sample Page ===
        self.ui.sampleBackButton.clicked.connect(self.goToDashboard)

        self.ui.addSensorButton.clicked.connect(self.goToAddSensor)
        self.ui.addSensorBackButton.clicked.connect(self.goToSample)
        # === Resources ===
        self.ui.boxBreathingBackButton.clicked.connect(self.goToResults)
        QScroller.grabGesture(self.ui.boxBreathingScrollArea.viewport(), QScroller.LeftMouseButtonGesture)
        QScroller.grabGesture(self.ui.testResultDetailsScrollArea.viewport(), QScroller.LeftMouseButtonGesture)

        self.ui.testResultsBackButton.clicked.connect(self.goToResults)

        # === Pair Watch ===
        self.ui.pairBackButton.clicked.connect(self.goToDashboard)
        self.ui.pairButton.clicked.connect(lambda: store_paired_watch_mac_from_ui(self.ui))

        # === Heart Ratte Page ===
        self.ui.heartRateBackButton.clicked.connect(self.goToDashboard)



        # Start heart rate serial listener in background
        self.serial_thread = threading.Thread(
           target=background_serial_heart_rate_listener, daemon=True
        )
        self.serial_thread.start()


    def goToHeartRate(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.heartRatePage)
        getHeartRate(self.ui)

    def goToAddSensor(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.newSensorPage)
    def goToPairWatch(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.watchPairingPage)

    def goToBoxBreathing(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.boxBreathingPage)
        boxBreathing(self.ui)
    def goToGroundingSession(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.groundingSessionPage)
        run_grounding_session(self.ui)
    def goToRegister(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.registerScreen)
    def goToLogin(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.loginScreen)
    def goToEntry(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.entryScreen)
    def goToDashboard(self):
        # Stop camera if it's running
        if hasattr(self.ui, "camera_stop_camera") and callable(self.ui.camera_stop_camera):
            try:
                self.ui.camera_stop_camera()
            except Exception as e:
                print(f"[WARN] Could not stop camera: {e}")
        self.tomoFaceAnimation.start()
        self.ui.stackedWidget.setCurrentWidget(self.ui.Dashboard)
    def goToDSMLevelOne(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.takeDSMLevelOnePage)

    def powerOff(self):
        print("[INFO] Shutting down LLM worker...")
        self.llm_job_queue.put(None)  # Signal worker to shut down
        self.llm_worker_process.join(timeout=5)  # Wait for up to 5 seconds for clean exit
        print("[INFO] LLM worker process terminated.")
        sys.exit()

    def signout(self):
        logout()
        self.goToEntry()
    def goToResults(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.resultsPage)
        load_all_dsm_graphs(self.ui)
        load_resources(self.ui)
        self.ui.tryGroundingSessionButton.clicked.connect(self.goToGroundingSession)
        #=== Resources  - Box Breathing ===
        self.ui.tryBoxBreathingButton.clicked.connect(self.goToBoxBreathing)

    def goToSample(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.takeSamplePage)

    def handle_start_recording(self):
        self.mic.start_recording()

    def handle_stop_recording(self):
        self.mic.stop_recording(self.ui)

    def notification(self):
        self.play_sound("menuPop")
        QTimer.singleShot(500, lambda: (
                self.ui.stackedWidget.setCurrentWidget(self.ui.notificationPage),
                notification(self.ui)
            ))

    def submitAccount(self):
        msg = registerSubmit(self.ui)
        if msg == "All Fields Not Filled":
            QMessageBox.warning(self, "Register Not Complete", "Not all fields were filled")
        if msg == "Complete":
            QMessageBox.information(self, "Register Complete", "You were successfully registered!")
            self.goToEntry()
    def submitLogin(self):
        msg = loginSubmit(self.ui)
        if msg == "All Fields Not Filled":
            QMessageBox.warning(self, "Register Not Complete", "Not all fields were filled")
        if msg == "Failed Login":
            QMessageBox.critical(self, "Failed Login", "Username or Password Incorrect.\n Please try again.")
        if msg == "Complete":
            QMessageBox.information(self, "Login Successful", "You are logged in!")
            self.goToDashboard()

    def notificationCheck(self):
        checkNotification(self.ui)

    def play_sound(self, sound_name):
        def _play():
            sound_files = {
                "menuPop": "menuPop.wav",
                "uiNav": "uiNav.wav",
            }
            filename = sound_files.get(sound_name)
            if filename:
                sound_path = os.path.join("Assets", "SoundEffects", filename)
                if os.path.exists(sound_path):
                    try:
                        import sounddevice as sd
                        import wave
                        import numpy as np
                        with wave.open(sound_path, "rb") as wf:
                            data = wf.readframes(wf.getnframes())
                            arr = np.frombuffer(data, dtype=np.int16)
                            sd.play(arr, wf.getframerate())
                            sd.wait()
                    except Exception as e:
                        print(f"[ERROR] Could not play sound: {e}")
                else:
                    print(f"[WARN] Sound file not found: {sound_path}")
            else:
                print(f"[WARN] Unknown sound: {sound_name}")




if __name__ == "__main__":


    llm_job_queue = multiprocessing.Queue()
    llm_worker_process = multiprocessing.Process(
        target=run_llm_worker, args=(llm_job_queue,), daemon=True
    )
    llm_worker_process.start()

    app = QApplication(sys.argv)
    widget = MainWindow(llm_job_queue=llm_job_queue, llm_worker_process=llm_worker_process)  # <-- pass both
    widget.showFullScreen()
    sys.exit(app.exec())
