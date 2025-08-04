from PySide6.QtWidgets import QLineEdit, QComboBox, QPushButton
from NotificationManager import sendLog
import os
import json
from datetime import datetime
from PySide6.QtCore import Qt


def run_grounding_session(ui):
    sendLog("User started Grounding Session")
    grounding_steps = [
        ("Name 5 things you can see", 5),
        ("Name 4 things you can touch", 4),
        ("Name 3 things you can hear", 3),
        ("Name 2 things you can smell", 2),
        ("Name 1 thing you can taste", 1),
    ]
    current_idx = 0
    answers = []
    entry_fields = []
    review_box = None  # For review input
    submit_btn = None  # For submit button

    # --- Helper to get username and session save path ---
    def get_user_and_session_path():
        user_json_path = "TomoBrain/Data/Users/current_user.json"
        if not os.path.exists(user_json_path):
            print(f"[ERROR] No current user at {user_json_path}")
            return None, None
        with open(user_json_path, "r", encoding="utf-8") as f:
            user_data = json.load(f)
        username = user_data.get("username")
        if not username:
            print("[ERROR] Username not found in current_user.json")
            return None, None
        sessions_dir = f"TomoBrain/Data/Users/{username}/Sessions"
        os.makedirs(sessions_dir, exist_ok=True)
        return username, sessions_dir

    def check_entries_filled():
        filled = all(e.text().strip() for e in entry_fields)
        ui.groundingNextpushButton.setEnabled(filled)

    def show_step(idx):
        nonlocal entry_fields
        ui.groundingNextpushButton.setVisible(True)
        ui.groundingNextpushButton.setEnabled(False)
        question, num_fields = grounding_steps[idx]
        ui.groundingQuestionLabel.setText(question)
        entry_fields = []

        layout = ui.groundingEntry
        while layout.count():
            item = layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        for i in range(num_fields):
            line_edit = QLineEdit()
            line_edit.setPlaceholderText(f"Enter {i+1}")
            line_edit.setMinimumHeight(44)   # or higher
            line_edit.setMinimumWidth(200)   # optional
            line_edit.setStyleSheet("font-size:20px")
            line_edit.textChanged.connect(check_entries_filled)
            layout.addWidget(line_edit)
            entry_fields.append(line_edit)

    def show_review():
        nonlocal review_box, submit_btn
        layout = ui.groundingEntry
        while layout.count():
            item = layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        ui.groundingQuestionLabel.setText("How would you rate this grounding session (1–5)?")

        # Review dropdown (1-5)
        review_box = QComboBox()
        review_box.addItems([str(i) for i in range(1, 6)])
        layout.addWidget(review_box)

        # Submit button
        submit_btn = QPushButton("Submit")
        layout.addWidget(submit_btn)

        def handle_submit():
            review_score = review_box.currentText()
            print("Grounding answers:", answers)
            print("Review score:", review_score)
            sendLog("User Completed Grounding Session")

            # Save session file
            username, sessions_dir = get_user_and_session_path()
            if sessions_dir:
                dt_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                session_path = os.path.join(sessions_dir, f"grounding_session_{dt_str}.json")
                session_data = {review_score: answers}
                try:
                    with open(session_path, "w", encoding="utf-8") as f:
                        json.dump(session_data, f, indent=4)
                    print(f"[INFO] Saved session to {session_path}")
                except Exception as e:
                    print(f"[ERROR] Could not save session: {e}")

            # Return to dashboard
            ui.stackedWidget.setCurrentWidget(ui.Dashboard)

        submit_btn.clicked.connect(handle_submit)
        ui.groundingNextpushButton.setVisible(False)

    def go_next():
        nonlocal current_idx
        user_answers = [e.text().strip() for e in entry_fields]
        answers.append(user_answers)
        current_idx += 1
        if current_idx < len(grounding_steps):
            show_step(current_idx)
        else:
            show_review()

    ui.groundingNextpushButton.clicked.connect(go_next)
    show_step(current_idx)
from PySide6.QtGui import QMovie

from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtGui import QFont

def boxBreathing(ui):
    """
    Display a box breathing info page with intro, GIF, and instructions,
    inside the boxBreathingScrollArea.
    """
    gif_path = "Assets/boxBreathing.gif"  # Update as needed

    # Get the scroll area's widget (or create one)
    scroll_widget = ui.boxBreathingScrollArea.widget()
    if scroll_widget is None:
        scroll_widget = QWidget()
        ui.boxBreathingScrollArea.setWidget(scroll_widget)

    # Transparent background for scroll area widget
    scroll_widget.setStyleSheet("background: transparent;")
    scroll_widget.setStyleSheet("border: none")
    # Set or reset the vertical layout
    layout = scroll_widget.layout()
    if layout is None:
        layout = QVBoxLayout(scroll_widget)
    else:
        # Remove old contents
        while layout.count():
            item = layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

    # 1. Top explanation label
    intro_text = (
        "Box breathing is a simple and effective technique used to manage stress and anxiety by focusing on slow, "
        "intentional breaths. This structured method, sometimes called four-square breathing, can be practiced anywhere "
        "and is commonly used to bring a sense of calm and control during overwhelming moments. By intentionally "
        "regulating your breathing, you help your mind and body return to a more relaxed state."
    )
    intro_label = QLabel(intro_text)
    intro_label.setWordWrap(True)
    intro_label.setStyleSheet("background: transparent; color:black;")
    # Bold font
    font = intro_label.font()
    font.setBold(True)
    intro_label.setFont(font)

    # 2. GIF label
    gif_label = QLabel()
    gif_label.setAlignment(Qt.AlignCenter)
    gif_label.setScaledContents(True)
    gif_label.setFixedHeight(300)
    gif_label.setStyleSheet("background: transparent;")
    movie = QMovie(gif_path)
    movie.setScaledSize(gif_label.size())
    gif_label.setMovie(movie)
    movie.start()

    # 3. Instruction label
    instruction_text = (
        "To perform box breathing, begin by sitting comfortably with your feet on the floor and your back straight. "
        "Inhale slowly through your nose to a count of four, feeling your lungs fill gently. Hold your breath for a count of four, "
        "keeping your body relaxed. Exhale slowly through your mouth for four seconds, then pause and hold your breath again for "
        "another count of four. Repeat this cycle for at least four rounds, or as long as feels comfortable. If counting to four feels "
        "too difficult, you can use a three-second count for each step instead.\n\n"
        "The purpose of box breathing is to activate your body’s relaxation response, signaling your brain that you are safe and helping to "
        "slow your heart rate and lower blood pressure. This technique can improve focus, emotional regulation, and mental clarity, "
        "making it a useful tool to practice daily or whenever you need to reset and regain a sense of calm."
    )
    instruction_label = QLabel(instruction_text)
    instruction_label.setWordWrap(True)
    instruction_label.setStyleSheet("background: transparent; color:black;")
    instruction_label.setFont(font)  # Also bold

    # Add to layout in order
    layout.addWidget(intro_label)
    layout.addWidget(gif_label)
    layout.addWidget(instruction_label)
    layout.addStretch()

