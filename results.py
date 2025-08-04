import os
import json
from datetime import datetime
import shutil
from PySide6.QtWidgets import QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QLineEdit
from PySide6.QtCore import QTimer
from PySide6.QtGui import QFont


def load_all_dsm_graphs(ui):

    user_json = "TomoBrain/Data/Users/current_user.json"
    if not os.path.exists(user_json):
        print("User not found!")
        return

    with open(user_json) as f:
        user_data = json.load(f)
    username = user_data.get("username", "")
    if not username:
        print("Username missing!")
        return

    # Transparent background for scroll area and its contents
    scroll_widget = ui.resultsScrollAreaWidgetContents
    scroll_widget.setStyleSheet("background: transparent;")
    ui.resultsScrollArea.setStyleSheet("background: transparent; border: none;")

    if scroll_widget.layout() is None:
        layout = QVBoxLayout(scroll_widget)
    else:
        layout = scroll_widget.layout()

    while layout.count():
        item = layout.takeAt(0)
        if item.widget():
            item.widget().deleteLater()

    test_file_map = {
        "dsm_level_one_results.json":              ("DSM Level One", "#42A5F5"),
        "dsm_level_two_depression_results.json":   ("DSM Level Two Depression", "#1DE9B6"),
        "dsm_level_two_anxiety_results.json":      ("DSM Level Two Anxiety", "#FFA726"),
        "dsm_level_two_anger_results.json":        ("DSM Level Two Anger", "#ef5350"),
        "dsm_level_two_mania_results.json":        ("DSM Level Two Mania", "#ab47bc"),
        "dsm_level_two_somatic_symptom_results.json": ("DSM Level Two Somatic Symptom", "#8d6e63"),
        "dsm_level_two_sleep_disturbance_results.json": ("DSM Level Two Sleep Disturbance", "#64b5f6"),
        "dsm_level_two_substance_use_results.json":    ("DSM Level Two Substance Use", "#ff7043"),
        "dsm_level_two_repetitive_thoughts_behaviors_results.json": ("DSM Level Two Repetitive Thoughts & Behaviors", "#bdb76b"),
        "dsm_level_two_irritability_results.json": ("DSM Level Two Irritability", "#ffd700"),
    }

    results_dir = f"TomoBrain/Data/Users/{username}/Results"

    for fname, (test_label, color) in test_file_map.items():
        results_file = os.path.join(results_dir, fname)
        if not os.path.exists(results_file):
            continue
        with open(results_file) as f:
            all_results = json.load(f)
        if not all_results:
            continue

        for key in sorted(all_results.keys(), reverse=True):
            if "_" in key:
                timestamp = key.split("_")[-2] + " " + key.split("_")[-1].replace("-", ":")
            else:
                timestamp = key

            # Unified card: bullet, label, and button all on one glass card
            row_widget = QWidget()
            row_layout = QHBoxLayout(row_widget)
            row_layout.setContentsMargins(22, 8, 22, 8)  # Nicely spaced
            row_layout.setSpacing(16)

            # Glassmorphism card style for the whole row (no extra card under bullet/label)
            row_widget.setStyleSheet("""
                QWidget {
                    border: 1.4px solid rgba(60,60,60,0.44);
                    border-radius: 22px;
                    background: rgba(32, 40, 54, 0.40); /* Translucent, glassy */
                    margin-bottom: 13px;
                    backdrop-filter: blur(8px);
                }
            """)

            bullet = QLabel("●")
            bullet.setStyleSheet(f"""
                QLabel {{
                    color: {color};
                    font-size: 24px;
                    font-weight: bold;
                    background: transparent;
                    margin-left: 6px;
                    margin-right: 14px;
                    border: none;
                }}
            """)

            label = QLabel(f"{test_label} {timestamp}")
            label.setStyleSheet(f"""
                QLabel {{
                    font-size: 20px;
                    color: {color};
                    font-weight: bold;
                    background: transparent;
                    border: none;
                }}
            """)
            label.setWordWrap(True)

            button = QPushButton("View Test")
            button.setStyleSheet(f"""
                QPushButton {{
                    background-color: {color};
                    color: #232629;
                    font-weight: bold;
                    border-radius: 12px;
                    padding: 7px 28px;
                    margin-left: 20px;
                }}
                QPushButton:hover {{
                    background-color: #1976D2;
                }}
            """)

            # Connect the button to showTestDetail
            def handler_factory(fname, result_key):
                return lambda: showTestDetail(ui, fname, result_key)
            button.clicked.connect(handler_factory(fname, key))

            row_layout.addWidget(bullet)
            row_layout.addWidget(label)
            row_layout.addStretch()
            row_layout.addWidget(button)
            layout.addWidget(row_widget)

    layout.addStretch()

import pandas as pd
from PySide6.QtWidgets import QVBoxLayout, QWidget, QLabel
from PySide6.QtGui import QFont

def showTestDetail(ui, fname, key):
    """
    Display a detailed view for a specific DSM test and timestamp.
    Assumes you have a details page/area and a scroll area for the details (e.g. ui.testResultDetailsScrollArea)
    """
    user_json = "TomoBrain/Data/Users/current_user.json"
    with open(user_json) as f:
        user_data = json.load(f)
    username = user_data.get("username", "")
    if not username:
        print("Username missing!")
        return

    results_file = f"TomoBrain/Data/Users/{username}/Results/{fname}"
    if not os.path.exists(results_file):
        print("Result file not found:", results_file)
        return

    with open(results_file) as f:
        all_results = json.load(f)
    if key not in all_results:
        print("Result not found:", key)
        return
    result = all_results[key]

    # --- LOAD ORIGINAL QUESTIONS FROM EXCEL ---
    excel_name = fname.replace("_results.json", ".xlsx")
    excel_path = f"TomoBrain/Data/Tests/{excel_name}"

    # Try to get correct sheet (Adult/Child)
    try:
        with open("TomoBrain/Data/Users/current_user.json") as f:
            user_data = json.load(f)
        age = int(user_data.get("age", 0))
        is_adult = age >= 18
        sheet = "Adult" if is_adult else "Child"
    except Exception:
        sheet = "Adult"

    # Load questions list from Excel
    try:
        df = pd.read_excel(excel_path, sheet_name=sheet, header=None)
        questions_list = df[0].dropna().tolist()
    except Exception as e:
        print(f"Could not load Excel questions: {e}")
        questions_list = []

    # Switch to the details page
    ui.stackedWidget.setCurrentWidget(ui.testResultDetailsPage)

    # Get the scroll area contents
    scroll_widget = ui.testResultDetailsScrollArea.widget()
    if scroll_widget is None:
        scroll_widget = QWidget()
        ui.testResultDetailsScrollArea.setWidget(scroll_widget)


    layout = scroll_widget.layout()
    if layout is None:
        layout = QVBoxLayout(scroll_widget)
    else:
        while layout.count():
            item = layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

    # Show the test title, timestamp, score, and all question/answer pairs
    #title = QLabel(f"{fname.replace('_results.json', '').replace('_', ' ').title()} — {key.split('_')[-2]} {key.split('_')[-1]}")
    #title.setFont(QFont("Arial", 14, QFont.Bold))
    #layout.addWidget(title)
    ui.testDetialsLabel.setText(f"{fname.replace('_results.json', '').replace('_', ' ').title()} — {key.split('_')[-2]} {':'.join(key.split('_')[-1].split('-')[:2])}")
    ui.testDetialsLabel.setStyleSheet("color:black;")

    score = result.get("total_raw_score") or result.get("raw_total") or result.get("used_score")
    if score is not None:
        score_lbl = QLabel(f"Total Score: {score}")
        score_lbl.setStyleSheet("qproperty-alignment: 'AlignCenter';color:black; font-size:20px;")
        layout.addWidget(score_lbl)

    questions = result.get("questions", {})
    for qnum, qdata in questions.items():
        # Prefer saved question text if present, otherwise look up in Excel
        question_text = qdata.get('question')
        if not question_text:
            try:
                idx = int(qnum.lstrip('Q')) - 1
                question_text = questions_list[idx] if idx < len(questions_list) else qnum
            except Exception:
                question_text = qnum

        answer = qdata.get('answer', qdata.get('answer_text', ''))
        score_value = qdata.get('score', '')
        qlbl = QLabel(f"<b>Q:</b> {question_text}<br><b>Your answer:</b> {answer} (Score: {score_value})")
        qlbl.setStyleSheet("qproperty-alignment: 'AlignCenter'; color:black; font-size:20px;")
        qlbl.setWordWrap(True)
        layout.addWidget(qlbl)

    layout.addStretch()






def load_notes(ui, mic):
    user_json = "TomoBrain/Data/Users/current_user.json"
    if not os.path.exists(user_json):
        print("User not found!")
        return

    with open(user_json) as f:
        user_data = json.load(f)
    username = user_data.get("username", "")
    if not username:
        print("Username missing!")
        return

    inprogress_path = f"TomoBrain/Data/Users/{username}/Journal/in_progress_note.json"

    scroll_widget = ui.notesScrollAreaWidgetContents
    scroll_widget.setStyleSheet("background: transparent;")
    ui.notesScrollArea.setStyleSheet("background: transparent; border: none;")

    if scroll_widget.layout() is None:
        layout = QVBoxLayout(scroll_widget)
    else:
        layout = scroll_widget.layout()

    for i in reversed(range(layout.count())):
        item = layout.itemAt(i)
        widget = item.widget()
        if widget and getattr(widget, "objectName", lambda: "")() != "addNoteButton":
            widget.setParent(None)

    if hasattr(ui, "addNoteButton"):
        add_btn = ui.addNoteButton
        add_btn.setParent(None)
        layout.insertWidget(0, add_btn)
        try:
            add_btn.clicked.disconnect()
        except Exception:
            pass
        add_btn.clicked.connect(lambda: add_note_row())
    else:
        print("No addNoteButton found on ui!")
        return

    def save_in_progress(note, progress, state):
        data = {
            "note_title": note,
            "progress": progress,
            "state": state
        }
        os.makedirs(os.path.dirname(inprogress_path), exist_ok=True)
        with open(inprogress_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    def clear_in_progress():
        if os.path.exists(inprogress_path):
            os.remove(inprogress_path)

    def add_note_row(restored=None):
        row_widget = QWidget()
        row_widget.setStyleSheet("""
            QWidget {
                border: 1.4px solid rgba(60,60,60,0.44);
                border-radius: 16px;
                background: rgba(32, 40, 54, 0.40);
                margin-bottom: 13px;
                backdrop-filter: blur(8px);
            }
        """)
        row_layout = QHBoxLayout(row_widget)
        row_layout.setContentsMargins(10, 10, 10, 10)
        row_layout.setSpacing(18)

        note_title = QLineEdit()
        note_title.setPlaceholderText("Enter note title...")
        note_title.setStyleSheet("""
            QLineEdit {
                font-size: 18px;
                color: #eaf6ff;
                background: rgba(0,0,0,0.10);
                border: none;
                border-radius: 6px;
                padding: 6px 12px;
                min-width: 250px;
                font-weight: bold;
            }
        """)
        if restored and "note_title" in restored:
            note_title.setText(restored["note_title"])
        row_layout.addWidget(note_title)

        btn_start = QPushButton("Start Recording")
        btn_stop = QPushButton("Stop Recording")
        btn_done = QPushButton("Done")
        btn_stop.setEnabled(False)
        btn_done.setEnabled(False)

        for btn, color in [(btn_start, "#40c057"), (btn_stop, "#e67e22"), (btn_done, "#1976D2")]:
            btn.setStyleSheet(f"""
                QPushButton {{
                    background-color: {color};
                    color: #f7f7f7;
                    font-weight: bold;
                    border-radius: 8px;
                    padding: 5px 16px;
                    min-width: 60px;
                }}
                QPushButton:hover {{
                    background-color: #232629;
                }}
            """)

        progress_label = None

        if restored:
            progress_label = QLabel(restored["progress"])
            progress_label.setObjectName("progressLabel")
            progress_label.setStyleSheet("""
                QLabel {
                    font-size: 17px;
                    color: #eaf6ff;
                    font-weight: bold;
                    padding: 8px 10px 8px 18px;
                    border-radius: 11px;
                    background: rgba(23,33,45,0.23);
                    margin-bottom: 8px;
                }
            """)
            layout.insertWidget(1, progress_label)
            if restored["state"] == "recording":
                btn_start.setEnabled(False)
                btn_stop.setEnabled(True)
                btn_done.setEnabled(False)
            elif restored["state"] == "processing":
                btn_start.setEnabled(False)
                btn_stop.setEnabled(False)
                btn_done.setEnabled(True)

        note_folder = None

        def start_rec():
            nonlocal progress_label, note_folder
            safe_title = "".join(c for c in note_title.text().strip() if c.isalnum() or c in (' ', '_')).strip().replace(" ", "_")
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            note_folder = os.path.join(
                f"TomoBrain/Data/Users/{username}/Journal", f"{safe_title}_{timestamp}"
            )
            os.makedirs(note_folder, exist_ok=True)

            if not progress_label:
                progress_label = QLabel("Recording...")
                progress_label.setObjectName("progressLabel")
                progress_label.setStyleSheet("""
                    QLabel {
                        font-size: 17px;
                        color: #eaf6ff;
                        font-weight: bold;
                        padding: 8px 10px 8px 18px;
                        border-radius: 11px;
                        background: rgba(23,33,45,0.23);
                        margin-bottom: 8px;
                    }
                """)
                layout.insertWidget(1, progress_label)
            else:
                progress_label.setText("Recording...")

            save_in_progress(note_title.text(), "Recording...", "recording")
            if mic is not None:
                mic.start_recording()
                btn_start.setEnabled(False)
                btn_stop.setEnabled(True)
                btn_done.setEnabled(False)
            else:
                progress_label.setText("Mic not found!")

        def stop_rec():
            nonlocal progress_label, note_folder
            if progress_label:
                progress_label.setText("Processing...")
                save_in_progress(note_title.text(), "Processing...", "processing")
            if mic is not None:
                # --- Pass NO progress_label (None) to avoid pickle error!
                mic.stop_recording(ui, save_dir=note_folder, progress_label=progress_label, llm_model_path="TomoBrain/Models/Phi-3-mini-4k-instruct-q4.gguf")
                # === Start polling for done.txt ===
                timer = QTimer()
                timer.setInterval(1000)
                def poll_status():
                    status_path = os.path.join(note_folder, "done.txt")
                    if os.path.exists(status_path):
                        progress_label.setText("Done!")
                        timer.stop()
                timer.timeout.connect(poll_status)
                timer.start()
                btn_stop.setEnabled(False)
                btn_done.setEnabled(True)
            else:
                if progress_label:
                    progress_label.setText("Mic not found!")

        def done_note():
            nonlocal progress_label, note_folder
            note = note_title.text().strip()
            if not note:
                if progress_label:
                    progress_label.setText("Please enter a note title.")
                return
            clear_in_progress()
            # --- Save note.json metadata in note_folder ---
            note_metadata = {
                "title": note,
                "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            }
            if note_folder:
                with open(os.path.join(note_folder, "note.json"), "w", encoding="utf-8") as f:
                    json.dump(note_metadata, f, indent=2)
            safe_title = "".join(c for c in note if c.isalnum() or c in (' ', '_')).strip().replace(" ", "_")
            timestamp = None
            if note_folder:
                timestamp = os.path.basename(note_folder).split("_")[-1]
            # --- DELETE done.txt if it exists ---
            if note_folder:
                done_path = os.path.join(note_folder, "done.txt")
                if os.path.exists(done_path):
                    os.remove(done_path)
            display_row = make_note_card(note, timestamp or "", note_folder, ui)
            layout.insertWidget(1, display_row)

            row_widget.setParent(None)
            if progress_label:
                progress_label.setParent(None)

        btn_start.clicked.connect(start_rec)
        btn_stop.clicked.connect(stop_rec)
        btn_done.clicked.connect(done_note)

        row_layout.addWidget(btn_start)
        row_layout.addWidget(btn_stop)
        row_layout.addWidget(btn_done)
        row_layout.addStretch()

        layout.insertWidget(1, row_widget)

    def make_note_card(note, timestamp, folder_path=None, ui=None):
        display_row = QWidget()
        display_row.setStyleSheet("""
            QWidget {
                border: 1.4px solid rgba(60,60,60,0.44);
                border-radius: 16px;
                background: rgba(32, 40, 54, 0.38);
                margin-bottom: 13px;
                backdrop-filter: blur(8px);
            }
        """)
        display_layout = QHBoxLayout(display_row)
        display_layout.setContentsMargins(10, 10, 10, 10)
        display_layout.setSpacing(18)

        card_label = QLabel(f"{note} {timestamp}")
        card_label.setStyleSheet("""
            QLabel {
                font-size: 17px;
                color: #1DE9B6;
                font-weight: bold;
                background: transparent;
                border: none;
            }
        """)
        card_label.setWordWrap(True)

        btn_play = QPushButton("Play Note")
        btn_view = QPushButton("View Note")
        #btn_recom = QPushButton("View Recommendation")
        #for btn, color in [(btn_play, "#40c057"), (btn_view, "#1976D2"), (btn_recom, "#1976D2")]:
        for btn, color in [(btn_play, "#40c057"), (btn_view, "#1976D2")]:

            btn.setStyleSheet(f"""
                QPushButton {{
                    background-color: {color};
                    color: #f7f7f7;
                    font-weight: bold;
                    border-radius: 8px;
                    padding: 5px 18px;
                }}
                QPushButton:hover {{
                    background-color: #232629;
                }}
            """)

        def play_audio():
                if not folder_path:
                    print("[WARN] No folder path for this note.")
                    return
                audio_path = os.path.join(folder_path, "audio.wav")
                if not os.path.exists(audio_path):
                    print(f"[WARN] No audio file at {audio_path}")
                    return
                import sounddevice as sd
                import wave
                import numpy as np
                try:
                    with wave.open(audio_path, "rb") as wf:
                        data = wf.readframes(wf.getnframes())
                        arr = np.frombuffer(data, dtype=np.int16)
                        sd.play(arr, wf.getframerate())
                        sd.wait()
                except Exception as e:
                    print(f"[ERROR] Could not play audio: {e}")
        def view_note():
            if not folder_path:
                print("[WARN] No folder path for this note.")
                return
            transcript_path = os.path.join(folder_path, "transcript.txt")
            if not os.path.exists(transcript_path):
                print(f"[WARN] No transcript found at {transcript_path}")
                return
            with open(transcript_path, "r", encoding="utf-8") as f:
                note_text = f.read()
            # --- Extract title from folder name ---
            folder_name = os.path.basename(folder_path)
            parts = folder_name.rsplit("_", 2)
            if len(parts) == 3:
                note_title = parts[0]
            else:
                note_title = folder_name
            # Show the note text in the journalNote label
            note_title = note_title.replace("_", " ")
            if ui:
                ui.journalNote.setText(note_text)
                ui.journalTitle.setText(note_title)
                # Assuming you use a QStackedWidget or similar for page switching:
                ui.stackedWidget.setCurrentWidget(ui.journalTextPage)
            else:
                print("[WARN] No UI object to update page/label.")
        def view_recom():
            if not folder_path:
                print("[WARN] No folder path for this note.")
                return
            recom_path = os.path.join(folder_path, "UserRecommendation.txt")
            if not os.path.exists(recom_path):
                print(f"[WARN] No recommendation found at {recom_path}")
                return
            with open(recom_path, "r", encoding="utf-8") as f:
                rec_text = f.read()
            if ui:
                ui.journalRecomLabel.setText(rec_text)
                # Assuming you use a QStackedWidget or similar for page switching:
                ui.stackedWidget.setCurrentWidget(ui.journalReccomendationpage)
            else:
                print("[WARN] No UI object to update page/label.")


        btn_view.clicked.connect(view_note)

        btn_play.clicked.connect(play_audio)

        #btn_recom.clicked.connect(view_recom)

        display_layout.addWidget(card_label)
        display_layout.addWidget(btn_play)
        display_layout.addWidget(btn_view)
        #display_layout.addWidget(btn_recom)
        display_layout.addStretch()
        return display_row

    # --- Load existing notes ---
    notes_dir = f"TomoBrain/Data/Users/{username}/Journal"
    existing_notes = []
    if os.path.exists(notes_dir):
        for folder in os.listdir(notes_dir):
            folder_path = os.path.join(notes_dir, folder)
            note_json = os.path.join(folder_path, "note.json")
            if os.path.isdir(folder_path) and os.path.exists(note_json):
                try:
                    with open(note_json, "r", encoding="utf-8") as f:
                        note_data = json.load(f)
                        created = note_data.get("created", folder.split("_")[-1])
                        title = note_data.get("title", folder)
                        existing_notes.append((created, title, folder))
                except Exception as e:
                    print(f"[WARN] Could not load note {note_json}: {e}")

    for created, title, folder in sorted(existing_notes, reverse=True):
        folder_path = os.path.join(notes_dir, folder)
        display_row = make_note_card(title, created, folder_path, ui)
        layout.addWidget(display_row)

    if os.path.exists(inprogress_path):
        try:
            with open(inprogress_path, "r", encoding="utf-8") as f:
                restored = json.load(f)
            add_note_row(restored=restored)
        except Exception as e:
            print(f"[WARN] Could not restore in-progress note: {e}")

    layout.addStretch()
