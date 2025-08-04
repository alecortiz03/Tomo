import os
import json
from datetime import datetime
from PySide6.QtWidgets import QLabel, QPushButton, QHBoxLayout, QWidget, QListWidgetItem, QVBoxLayout
from TakeDSMLevelOne import run_dsm_level_one_test, run_dsm_level_two_depression, run_dsm_level_two_anger, run_dsm_level_two_mania, run_dsm_level_two_irritability, run_dsm_level_two_anxiety, run_dsm_level_two_somatic_symptom, run_dsm_level_two_sleep_disturbance,  run_dsm_level_two_repetitive_thoughts_behaviors, run_dsm_level_two_substance_use




def load_user_notifications(ui):
    """
    Loads notifications for the current user and fills the notificationsScrollArea with notification rows.
    Each notification gets a Take Test button (if appropriate) and a Delete button.
    """

    # 1️⃣ Load current user
    users_file = "TomoBrain/Data/Users/current_user.json"
    if os.path.exists(users_file):
        with open(users_file) as f:
            user_data = json.load(f)
        username = user_data.get("username", "")
    else:
        print("No current user found!")
        return

    if not username:
        print("Username missing in current_user.json!")
        return

    notif_file = f"TomoBrain/Data/Users/{username}/notifications.json"
    print(f"Using notifications file: {notif_file}")

    # 2️⃣ Reference to your scroll area widget (set this objectName in Qt Designer!)
    scroll_widget = ui.notificationsScrollAreaWidgetContents

    # 3️⃣ Use a vertical layout for notifications
    if scroll_widget.layout() is None:
        layout = QVBoxLayout(scroll_widget)
    else:
        layout = scroll_widget.layout()

    # 4️⃣ Clear the layout
    while layout.count():
        item = layout.takeAt(0)
        if item.widget():
            item.widget().deleteLater()

    # 5️⃣ Load notifications
    notifications = []
    if os.path.exists(notif_file):
        with open(notif_file) as f:
            try:
                notifications = json.load(f)
                if not isinstance(notifications, list):
                    print("[WARN] notifications.json is not a list!")
                    notifications = []
            except Exception as e:
                print("[ERROR] Could not parse notifications.json:", e)

    # 6️⃣ Add notifications as styled rows
    for notif in notifications:
        # Create a QWidget to hold the row content
        row_widget = QWidget()
        row_layout = QHBoxLayout(row_widget)
        row_layout.setContentsMargins(10, 7, 10, 7)
        row_layout.setSpacing(12)

        # Colored bullet
        bullet = QLabel("●")
        bullet.setStyleSheet("""
            QLabel {
                color: black;
                font-size: 20px;
                font-weight: bold;
                margin-right: 8px;
                background: transparent;
                border: none;
            }
        """)

        # Notification text
        label = QLabel(notif)
        label.setStyleSheet("font-size: 16px; font-weight: bold; color: #1DE9B6;")
        label.setStyleSheet("""
        QLabel {
            color: black;
            font-size: 20px;
            font-weight: bold;
            margin-right: 8px;
            background: transparent;
            border: none;
        }
    """)
        label.setWordWrap(True)
        row_layout.addWidget(bullet)
        row_layout.addWidget(label)

        # Take Test button logic (same as before)
        def add_take_test_button(text, func, page):
            btn = QPushButton("Take Test")
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #1DE9B6;
                    color: #232629;
                    font-weight: bold;
                    border-radius: 8px;
                    padding: 4px 14px;
                }
                QPushButton:hover {
                    background-color: #14cfa2;
                }
            """)
            btn.clicked.connect(lambda: (ui.stackedWidget.setCurrentWidget(getattr(ui, page)), func(ui)))
            row_layout.addWidget(btn)

        if "Take DSM Level One" in notif:
            add_take_test_button("Take DSM Level One", run_dsm_level_one_test, "takeDSMLevelOnePage")
        if "Take DSM Level Two - Depression" in notif:
            add_take_test_button("Take DSM Level Two - Depression", run_dsm_level_two_depression, "DSMLevelTwoDepression")
        if "Take DSM Level Two - Anger" in notif:
            add_take_test_button("Take DSM Level Two - Anger", run_dsm_level_two_anger, "DSMLevelTwoAnger")
        if "Take DSM Level Two - Mania" in notif:
            add_take_test_button("Take DSM Level Two - Mania", run_dsm_level_two_mania, "DSMLevelTwoMania")
        if "Take DSM Level Two - Irritability" in notif:
            add_take_test_button("Take DSM Level Two - Irritability", run_dsm_level_two_irritability, "DSMLevelTwoIrritability")
        if "Take DSM Level Two - Anxiety" in notif:
            add_take_test_button("Take DSM Level Two - Anxiety", run_dsm_level_two_anxiety, "DSMLevelTwoAnxiety")
        if "Take DSM Level Two - Somatic Symptoms" in notif:
            add_take_test_button("Take DSM Level Two - Somatic Symptoms", run_dsm_level_two_somatic_symptom, "DSMLevelTwoSomaticSymptoms")
        if "Take DSM Level Two - Sleep Disturbance" in notif:
            add_take_test_button("Take DSM Level Two - Sleep Disturbance", run_dsm_level_two_sleep_disturbance, "DSMLevelTwoSleepDisturbance")
        if "Take DSM Level Two - Repetitive Thoughts & Behaviors" in notif:
            add_take_test_button("Take DSM Level Two - Repetitive Thoughts & Behaviors", run_dsm_level_two_repetitive_thoughts_behaviors, "DSMLevelTwoReptitiveThoughts")
        if "Take DSM Level Two - Substance Use" in notif:
            add_take_test_button("Take DSM Level Two - Substance Use", run_dsm_level_two_substance_use, "DSMLevelTwoSubstanceUse")

        # Delete button
        del_btn = QPushButton("Delete")
        del_btn.setStyleSheet("""
            QPushButton {
                background-color: #ef5350;
                color: white;
                font-weight: bold;
                border-radius: 8px;
                padding: 4px 14px;
            }
            QPushButton:hover {
                background-color: #b71c1c;
            }
        """)
        def delete_notification(_, text=notif):
            notifications.remove(text)
            with open(notif_file, "w") as f:
                json.dump(notifications, f, indent=4)
            load_user_notifications(ui)
        del_btn.clicked.connect(delete_notification)
        row_layout.addWidget(del_btn)

        row_layout.addStretch()

        # Card border/background
        row_widget.setStyleSheet("""
        QWidget {
            border: 1.4px solid rgba(60,60,60,0.44);
            border-radius: 16px;
            background: rgba(32, 40, 54, 0.38);
            margin-bottom: 13px;
            backdrop-filter: blur(8px);
        }
    """)

        layout.addWidget(row_widget)

    layout.addStretch()

    print(f"[INFO] Loaded {len(notifications)} notifications for user: {username}")

def checkNotification(ui):
        currentUserPath = "TomoBrain/Data/Users/current_user.json"
        if not os.path.exists(currentUserPath):
            return
        with open(currentUserPath) as f:
            user = json.load(f)
        username = list(user.values())[2]
        file_path = f"TomoBrain/Data/Users/{username}/notifications.json"  # adjust to your real path!
        if os.path.exists(file_path):
            try:
                with open(file_path) as f:
                    data = json.load(f)
                if isinstance(data, list):
                    count = len(data)
                    ui.notificationCountLabel.setText(f"{count}")
                    ui.notificationCountLabelResults.setText(f"{count}")
            except json.JSONDecodeError:
                ui.notificationCountLabel.setText("Error!")
        else:
            ui.notificationCountLabel.setText("0")
            ui.notificationCountLabelResults.setText("0")
def sendLog(message):
    # Step 1: Get current user's username
    user_json_path = "TomoBrain/Data/Users/current_user.json"
    if not os.path.exists(user_json_path):
        print(f"[ERROR] No current user at {user_json_path}")
        return False

    with open(user_json_path, "r", encoding="utf-8") as f:
        user_data = json.load(f)
    username = user_data.get("username")
    if not username:
        print("[ERROR] Username not found in current_user.json")
        return False

    # Step 2: Construct user logs path
    logs_dir = f"TomoBrain/Data/Users/{username}/Logs"
    os.makedirs(logs_dir, exist_ok=True)
    logs_path = os.path.join(logs_dir, "user_logs.json")

    # Step 3: Load existing logs (or create empty if new)
    if os.path.exists(logs_path):
        with open(logs_path, "r", encoding="utf-8") as f:
            try:
                logs = json.load(f)
            except Exception:
                logs = {}
    else:
        logs = {}

    # Step 4: Add new log entry
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logs[now_str] = message

    # Step 5: Write back to file
    with open(logs_path, "w", encoding="utf-8") as f:
        json.dump(logs, f, indent=4)

    print(f"[INFO] Log added for {username}: {now_str} -> {message}")
    return True
