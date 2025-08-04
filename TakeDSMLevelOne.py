import json
import os
import pandas as pd
from collections import defaultdict
from PySide6.QtWidgets import QPushButton
from datetime import datetime

def run_dsm_level_two_substance_use(ui):
    """
    DSM Level Two Substance Use (Adult/Child).
    Scores each question individually. Saves all answers and total score.
    Sends notifications/logs if substance use is detected.
    """
    import json, os
    from datetime import datetime
    selected_scores = {}
    selected_answers = {}
    current_idx = 0
    answer_buttons = []

    # Load user age and username
    with open("TomoBrain/Data/Users/current_user.json") as f:
        user_data = json.load(f)
    age = int(user_data["age"])
    username = user_data.get("username", "unknown")

    is_adult = age >= 18
    sheet = "Adult" if is_adult else "Child"
    ui.dsmLevelTwoSubstanceUseTitleLabel.setText(
        f"DSM Level Two Substance Use — {'Adult' if is_adult else 'Child'}"
    )
    print(f"[DEBUG] User age: {age} — Using sheet: {sheet}")

    import pandas as pd
    df = pd.read_excel(
        "TomoBrain/Data/Tests/dsm_level_two_substance_use.xlsx",
        sheet_name=sheet,
        header=None
    )
    questions = df[0].dropna().tolist()
    print(f"[DEBUG] Loaded {len(questions)} questions")

    # --- Word choices per age group
    if is_adult:
        labels = [
            ("Not at all (0)", 0),
            ("1 or 2 days (1)", 1),
            ("Several days (2)", 2),
            ("More than half the days (3)", 3),
            ("Nearly every day (4)", 4)
        ]
    else:
        labels = [
            ("Not at all (0)", 0),
            ("Less than a day or two (1)", 1),
            ("Several days (2)", 2),
            ("More than half the days (3)", 3),
            ("Nearly every day (4)", 4)
        ]

    def show_question(idx):
        nonlocal answer_buttons
        ui.dsmLevelTwoSubstanceUseNextButton.setEnabled(False)
        answer_buttons = []

        if idx >= len(questions):
            show_submit()
            return

        question = questions[idx]
        ui.dsmLevelTwoSubstanceUseLabel.setText(question)
        print(f"[DEBUG] Q{idx + 1}: {question}")

        # Clear previous buttons
        while ui.dsmLevelTwoSubstanceUseQuestionLayout.count():
            item = ui.dsmLevelTwoSubstanceUseQuestionLayout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        # Add answer buttons
        for text, score in labels:
            btn = QPushButton(text)
            btn.setStyleSheet("background-color: white; color: black; font-size:24px;")
            btn.clicked.connect(lambda _, s=score, t=text, b=btn: handle_answer(s, t, b, idx))
            ui.dsmLevelTwoSubstanceUseQuestionLayout.addWidget(btn)
            answer_buttons.append(btn)

    def handle_answer(score, answer_text, clicked_button, q_idx):
        selected_scores[q_idx] = score
        selected_answers[q_idx] = {"answer_text": answer_text, "score": score}
        for btn in answer_buttons:
            btn.setStyleSheet("background-color: white; color: black;")
        clicked_button.setStyleSheet("background-color: #008060; color: white;")
        print(f"[DEBUG] Q{q_idx + 1} | {answer_text} ({score})")
        ui.dsmLevelTwoSubstanceUseNextButton.setEnabled(True)

    def go_next():
        nonlocal current_idx
        current_idx += 1
        show_question(current_idx)

    def show_submit():
        ui.dsmLevelTwoSubstanceUseLabel.setText("All done! Click Submit to save your results.")
        while ui.dsmLevelTwoSubstanceUseQuestionLayout.count():
            item = ui.dsmLevelTwoSubstanceUseQuestionLayout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
        ui.dsmLevelTwoSubstanceUseNextButton.setVisible(False)
        submit_btn = QPushButton("Submit")
        submit_btn.setMinimumHeight(50)
        submit_btn.setStyleSheet("background-color: green; color: white; font-size: 18px;")
        submit_btn.clicked.connect(submit)
        ui.dsmLevelTwoSubstanceUseQuestionLayout.addWidget(submit_btn)
        print("[DEBUG] All cleared — Submit button shown!")

    def submit():
        total_raw = sum(selected_scores.values())
        num_positive = sum(1 for v in selected_scores.values() if v > 0)
        print(f"[RESULT] Raw Total: {total_raw}")

        # Notify/log for each specific substance used
        any_substance = False
        for idx, score in selected_scores.items():
            if score > 0:
                question = questions[idx]
                msg = f"Substance use reported: '{question}' — Severity: {selected_answers[idx]['answer_text']}"
                #sendNotification(msg)
                sendLog(msg)
                any_substance = True

        if any_substance:
            sendNotification("Some substance use was reported on Level Two Substance Use test.")
            sendLog("Positive substance use detected (one or more items > 0)")
        else:
            sendNotification("No substance use was reported on Level Two Substance Use test.")
            sendLog("No substance use detected (all items 0)")

        # Save results
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        result_key = f"dsm_level_two_substance_use_{timestamp}"
        results = {
            "questions": {
                f"Q{q + 1}": selected_answers[q] for q in selected_answers
            },
            "total_raw_score": total_raw,
            "num_items_positive": num_positive
        }
        results_dir = f"TomoBrain/Data/Users/{username}/Results"
        os.makedirs(results_dir, exist_ok=True)
        results_file = os.path.join(results_dir, "dsm_level_two_substance_use_results.json")
        all_results = {}
        if os.path.exists(results_file):
            with open(results_file, "r") as f:
                try:
                    all_results = json.load(f)
                except Exception:
                    all_results = {}
        all_results[result_key] = results
        with open(results_file, "w") as f:
            json.dump(all_results, f, indent=4)
        print(f"[INFO] Saved results to: {results_file}")
        ui.stackedWidget.setCurrentWidget(ui.Dashboard)

    ui.dsmLevelTwoSubstanceUseNextButton.setEnabled(False)
    ui.dsmLevelTwoSubstanceUseNextButton.setText("Next")
    ui.dsmLevelTwoSubstanceUseNextButton.clicked.connect(go_next)
    show_question(current_idx)



def run_dsm_level_two_repetitive_thoughts_behaviors(ui):
    """
    DSM-5-TR Level 2 — Repetitive Thoughts and Behavior (Adult or Child).
    Dynamically loads correct sheet (Adult/Child), answers, handles scoring, saves, notifies, and logs.
    """
    import os
    import json
    import pandas as pd
    from datetime import datetime
    from PySide6.QtWidgets import QPushButton

    selected_scores = {}
    selected_answers = {}
    current_idx = 0
    answer_buttons = []

    # Load user + username
    with open("TomoBrain/Data/Users/current_user.json") as f:
        user_data = json.load(f)
    age = int(user_data.get("age", 0))
    username = user_data.get("username", "unknown")

    is_adult = age >= 18
    sheet = "Adult" if is_adult else "Child"
    ui.dsmLevelTwoRepetitiveThoughtsBehaviorsTitleLabel.setText(
        f"DSM Level Two — Repetitive Thoughts & Behaviors ({sheet})"
    )

    # Load appropriate sheet (Adult or Child)
    df = pd.read_excel(
        "TomoBrain/Data/Tests/dsm_level_two_repetitive_thoughts_behaviors.xlsx",
        sheet_name=sheet,
        header=None
    )
    df = df.dropna(how='all')
    questions = df[0].tolist()
    all_answer_sets = df.iloc[:, 1:6].values.tolist()  # answers columns

    print(f"[DEBUG] User age: {age} — Using sheet: {sheet}")
    print(f"[DEBUG] Loaded {len(questions)} questions")

    def show_question(idx):
        nonlocal answer_buttons
        ui.dsmLevelTwoRepetitiveThoughtsBehaviorsNextButton.setEnabled(False)
        ui.dsmLevelTwoRepetitiveThoughtsBehaviorsNextButton.setVisible(True)
        answer_buttons = []

        if idx >= len(questions):
            show_submit()
            return

        question = questions[idx]
        answers = all_answer_sets[idx]
        ui.dsmLevelTwoRepetitiveThoughtsBehaviorsLabel.setText(question)
        print(f"[DEBUG] Q{idx + 1}: {question}")

        while ui.dsmLevelTwoRepetitiveThoughtsBehaviorsQuestionLayout.count():
            item = ui.dsmLevelTwoRepetitiveThoughtsBehaviorsQuestionLayout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        for score, text in enumerate(answers):
            btn = QPushButton(f"{text} ({score})")
            btn.setStyleSheet("background-color: white; color: black; font-size:24px;")
            btn.clicked.connect(lambda _, s=score, t=text, b=btn: handle_answer(s, t, b, idx))
            ui.dsmLevelTwoRepetitiveThoughtsBehaviorsQuestionLayout.addWidget(btn)
            answer_buttons.append(btn)

    def handle_answer(score, answer_text, clicked_button, q_idx):
        selected_scores[q_idx] = score
        selected_answers[q_idx] = {"answer_text": answer_text, "score": score}

        for btn in answer_buttons:
            btn.setStyleSheet("background-color: white; color: black;")
        clicked_button.setStyleSheet("background-color: #008060; color: white;")
        print(f"[DEBUG] Q{q_idx + 1} | {answer_text} ({score})")
        ui.dsmLevelTwoRepetitiveThoughtsBehaviorsNextButton.setEnabled(True)

    def go_next():
        nonlocal current_idx
        current_idx += 1
        show_question(current_idx)

    def show_submit():
        ui.dsmLevelTwoRepetitiveThoughtsBehaviorsLabel.setText("All done! Click Submit to save your results.")
        while ui.dsmLevelTwoRepetitiveThoughtsBehaviorsQuestionLayout.count():
            item = ui.dsmLevelTwoRepetitiveThoughtsBehaviorsQuestionLayout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
        ui.dsmLevelTwoRepetitiveThoughtsBehaviorsNextButton.setVisible(False)

        submit_btn = QPushButton("Submit")
        submit_btn.setMinimumHeight(50)
        submit_btn.setStyleSheet("background-color: green; color: white; font-size: 18px;")
        submit_btn.clicked.connect(submit)
        ui.dsmLevelTwoRepetitiveThoughtsBehaviorsQuestionLayout.addWidget(submit_btn)
        print("[DEBUG] All cleared — Submit button shown!")

    def submit():
        n_answered = len(selected_scores)
        n_items = len(questions)
        print(f"[RESULT] {n_answered}/{n_items} answered")

        if n_answered < n_items - 1:
            ui.dsmLevelTwoRepetitiveThoughtsBehaviorsLabel.setText(
                "Not enough items answered to score this test. Please answer at least 4 questions."
            )
            print("[WARN] Too many missing answers!")
            return

        raw_sum = sum(selected_scores.values())
        if n_answered < n_items:
            prorated = int(round(raw_sum * n_items / n_answered))
            used_score = prorated
            print(f"[RESULT] Prorated score ({raw_sum} × {n_items} / {n_answered}) = {used_score}")
        else:
            used_score = raw_sum

        avg_score = round(used_score / n_items, 2)

        severity = "None"
        if avg_score >= 4:
            severity = "Extreme"
            sendNotification("Extreme repetitive thoughts and behaviors detected.")
            sendLog("Extreme repetitive thoughts and behaviors detected")
        elif avg_score >= 3:
            severity = "Severe"
            sendNotification("Severe repetitive thoughts and behaviors detected.")
            sendLog("Severe repetitive thoughts and behaviors detected")
        elif avg_score >= 2:
            severity = "Moderate"
            sendNotification("Moderate repetitive thoughts and behaviors detected.")
            sendLog("Moderate repetitive thoughts and behaviors detected")
        elif avg_score >= 1:
            severity = "Mild"
            sendNotification("Mild repetitive thoughts and behaviors detected.")
            sendLog("Mild repetitive thoughts and behaviors detected")

        if used_score >= 8:
            sendNotification("Further OCD assessment may be needed (Score >= 8).")
            sendLog("OCD assessment recommended (Score >= 8)")

        print(f"[RESULT] Raw: {raw_sum}, Final Used Score: {used_score} — Avg: {avg_score} — Severity: {severity}")

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        result_key = f"dsm_level_two_repetitive_thoughts_behaviors_{timestamp}"

        results = {
            "questions": {
                f"Q{q + 1}": selected_answers[q] for q in selected_answers
            },
            "raw_total": raw_sum,
            "final_score": used_score,
            "average_score": avg_score,
            "severity": severity,
            "prorated": (n_answered != n_items)
        }

        results_dir = f"TomoBrain/Data/Users/{username}/Results"
        os.makedirs(results_dir, exist_ok=True)

        results_file = os.path.join(results_dir, "dsm_level_two_repetitive_thoughts_behaviors_results.json")
        all_results = {}
        if os.path.exists(results_file):
            with open(results_file, "r") as f:
                try:
                    all_results = json.load(f)
                except Exception:
                    all_results = {}
        all_results[result_key] = results
        with open(results_file, "w") as f:
            json.dump(all_results, f, indent=4)
        print(f"[INFO] Saved results to: {results_file}")

        ui.stackedWidget.setCurrentWidget(ui.Dashboard)

    ui.dsmLevelTwoRepetitiveThoughtsBehaviorsNextButton.setEnabled(False)
    ui.dsmLevelTwoRepetitiveThoughtsBehaviorsNextButton.setText("Next")
    ui.dsmLevelTwoRepetitiveThoughtsBehaviorsNextButton.setVisible(True)
    ui.dsmLevelTwoRepetitiveThoughtsBehaviorsNextButton.clicked.connect(go_next)

    show_question(current_idx)


def run_dsm_level_two_sleep_disturbance(ui):
    """
    DSM-5-TR Level 2 Sleep Disturbance (Child/Adolescent, 8 items, reverse scoring for 2,3,7,8).
    Prorates and saves, with full clinical cutoff logic.
    """
    import os
    import json
    import pandas as pd
    from datetime import datetime
    from PySide6.QtWidgets import QPushButton

    selected_scores = {}
    selected_answers = {}
    current_idx = 0
    answer_buttons = []

    # === Load user & questions ===
    with open("TomoBrain/Data/Users/current_user.json") as f:
        user_data = json.load(f)
    username = user_data.get("username", "unknown")
    ui.dsmLevelTwoSleepDisturbanceTitleLabel.setText("DSM Level Two — Sleep Disturbance (Child)")

    df = pd.read_excel(
        "TomoBrain/Data/Tests/dsm_level_two_sleep_disturbance.xlsx",
        header=None
    )
    questions = df[0].dropna().tolist()
    print(f"[DEBUG] Loaded {len(questions)} questions")

    # Reverse scored questions: index 1,2,6,7 (Python is 0-based)
    reverse_idx = {1, 2, 6, 7}

    labels = [
        "Not at all",
        "A little bit",
        "Somewhat",
        "Quite a bit",
        "Very much"
    ]

    def show_question(idx):
        nonlocal answer_buttons
        ui.dsmLevelTwoSleepDisturbanceNextButton.setEnabled(False)
        ui.dsmLevelTwoSleepDisturbanceNextButton.setVisible(True)  # <-- Fix: always show Next on questions
        answer_buttons = []

        if idx >= len(questions):
            show_submit()
            return

        question = questions[idx]
        ui.dsmLevelTwoSleepDisturbanceLabel.setText(question)
        print(f"[DEBUG] Q{idx + 1}: {question}")

        while ui.dsmLevelTwoSleepDisturbanceQuestionLayout.count():
            item = ui.dsmLevelTwoSleepDisturbanceQuestionLayout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        for i, text in enumerate(labels):
            # For reverse-scored, flip the score
            if idx in reverse_idx:
                score = 5 - i  # 0 -> 5, 1 -> 4, ..., 4 -> 1
            else:
                score = i + 1  # 0 -> 1, 1 -> 2, ..., 4 -> 5

            btn = QPushButton(f"{text} ({score})")
            btn.setStyleSheet("background-color: white; color: black; font-size:24px;")
            btn.clicked.connect(lambda _, s=score, t=text, b=btn: handle_answer(s, t, b, idx))
            ui.dsmLevelTwoSleepDisturbanceQuestionLayout.addWidget(btn)
            answer_buttons.append(btn)

    def handle_answer(score, answer_text, clicked_button, q_idx):
        selected_scores[q_idx] = score
        selected_answers[q_idx] = {"answer_text": answer_text, "score": score}

        for btn in answer_buttons:
            btn.setStyleSheet("background-color: white; color: black;")
        clicked_button.setStyleSheet("background-color: #008060; color: white;")
        print(f"[DEBUG] Q{q_idx + 1} | {answer_text} ({score})")
        ui.dsmLevelTwoSleepDisturbanceNextButton.setEnabled(True)

    def go_next():
        nonlocal current_idx
        current_idx += 1
        show_question(current_idx)

    def show_submit():
        # Clear all UI
        ui.dsmLevelTwoSleepDisturbanceLabel.setText("All done! Click Submit to save your results.")
        while ui.dsmLevelTwoSleepDisturbanceQuestionLayout.count():
            item = ui.dsmLevelTwoSleepDisturbanceQuestionLayout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
        ui.dsmLevelTwoSleepDisturbanceNextButton.setVisible(False)

        submit_btn = QPushButton("Submit")
        submit_btn.setMinimumHeight(50)
        submit_btn.setStyleSheet("background-color: green; color: white; font-size: 18px;")
        submit_btn.clicked.connect(submit)
        ui.dsmLevelTwoSleepDisturbanceQuestionLayout.addWidget(submit_btn)
        print("[DEBUG] All cleared — Submit button shown!")

    def submit():
        n_answered = len(selected_scores)
        print(f"[RESULT] {n_answered}/8 answered")
        n_items = 8

        if n_answered < 6:
            ui.dsmLevelTwoSleepDisturbanceLabel.setText(
                "Not enough items answered to score this test. Please answer at least 6 questions."
            )
            print("[WARN] Too many missing answers!")
            return

        raw_sum = sum(selected_scores.values())
        if n_answered < n_items:
            prorated = int(round(raw_sum * n_items / n_answered))
            used_score = prorated
            print(f"[RESULT] Prorated score ({raw_sum} × 8 / {n_answered}) = {used_score}")
        else:
            used_score = raw_sum

        # Severity interpretation (example, you may adjust cutoffs/messages)
        if used_score <= 12:
            severity = "Minimal"
        elif 13 <= used_score <= 20:
            severity = "Low"
            sendNotification("Low Sleep Disturbance Detected")
            sendLog("Low Sleep Disturbance Detected")
        elif 21 <= used_score <= 29:
            severity = "Medium"
            sendNotification("Medium Sleep Disturbance Detected")
            sendLog("Medium Sleep Disturbance Detected")
        elif used_score >= 30:
            severity = "High"
            sendNotification("High Sleep Disturbance Detected")
            sendLog("High Sleep Disturbance Detected")
        else:
            severity = "Unknown"

        print(f"[RESULT] Raw: {raw_sum}, Final Used Score: {used_score} — Severity: {severity}")

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        result_key = f"dsm_level_two_sleep_disturbance_{timestamp}"

        results = {
            "questions": {
                f"Q{q + 1}": selected_answers[q] for q in selected_answers
            },
            "raw_total": raw_sum,
            "used_score": used_score,
            "severity": severity,
            "prorated": (n_answered != n_items)
        }

        results_dir = f"TomoBrain/Data/Users/{username}/Results"
        os.makedirs(results_dir, exist_ok=True)

        results_file = os.path.join(results_dir, "dsm_level_two_sleep_disturbance_results.json")
        all_results = {}
        if os.path.exists(results_file):
            with open(results_file, "r") as f:
                try:
                    all_results = json.load(f)
                except Exception:
                    all_results = {}
        all_results[result_key] = results
        with open(results_file, "w") as f:
            json.dump(all_results, f, indent=4)
        print(f"[INFO] Saved results to: {results_file}")

        ui.stackedWidget.setCurrentWidget(ui.Dashboard)

    ui.dsmLevelTwoSleepDisturbanceNextButton.setEnabled(False)
    ui.dsmLevelTwoSleepDisturbanceNextButton.setText("Next")
    ui.dsmLevelTwoSleepDisturbanceNextButton.setVisible(True)
    ui.dsmLevelTwoSleepDisturbanceNextButton.clicked.connect(go_next)

    show_question(current_idx)




def run_dsm_level_two_somatic_symptom(ui):
    """
    DSM Level Two Somatic Symptom (PHQ-15) for Adult and Child.
    Scores, prorates for children, and saves results.
    """

    selected_scores = {}
    selected_answers = {}
    current_idx = 0
    answer_buttons = []

    # Load user age + username
    with open("TomoBrain/Data/Users/current_user.json") as f:
        user_data = json.load(f)
    age = int(user_data["age"])
    username = user_data.get("username", "unknown")

    is_adult = age >= 18
    sheet = "Adult" if is_adult else "Child"
    ui.dsmLevelTwoSomaticSymptomTitleLabel.setText(
        f"DSM Level Two Somatic Symptom — {'Adult' if is_adult else 'Child'}"
    )
    print(f"[DEBUG] User age: {age} — Using sheet: {sheet}")

    # Load questions
    df = pd.read_excel(
        "TomoBrain/Data/Tests/dsm_level_two_somatic_symptom.xlsx",
        sheet_name=sheet,
        header=None
    )
    questions = df[0].dropna().tolist()
    print(f"[DEBUG] Loaded {len(questions)} questions")

    def show_question(idx):
        nonlocal answer_buttons
        ui.dsmLevelTwoSomaticSymptomNextButton.setEnabled(False)
        answer_buttons = []

        if idx >= len(questions):
            show_submit()
            return

        question = questions[idx]
        ui.dsmLevelTwoSomaticSymptomLabel.setText(question)

        print(f"[DEBUG] Q{idx + 1}: {question}")

        while ui.dsmLevelTwoSomaticSymptomQuestionLayout.count():
            item = ui.dsmLevelTwoSomaticSymptomQuestionLayout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        labels = [
            ("Not bothered at all (0)", 0),
            ("Bothered a little (1)", 1),
            ("Bothered a lot (2)", 2)
        ]
        for text, score in labels:
            btn = QPushButton(text)
            btn.setStyleSheet("background-color: white; color: black; font-size:24px;")
            btn.clicked.connect(lambda _, s=score, t=text, b=btn: handle_answer(s, t, b, idx))
            ui.dsmLevelTwoSomaticSymptomQuestionLayout.addWidget(btn)
            answer_buttons.append(btn)

        # Make sure Next button is visible on every question except after last Next
        ui.dsmLevelTwoSomaticSymptomNextButton.setVisible(True)

    def handle_answer(score, answer_text, clicked_button, q_idx):
        selected_scores[q_idx] = score
        selected_answers[q_idx] = {"answer_text": answer_text, "score": score}

        for btn in answer_buttons:
            btn.setStyleSheet("background-color: white; color: black;")
        clicked_button.setStyleSheet("background-color: #008060; color: white;")

        print(f"[DEBUG] Q{q_idx + 1} | {answer_text} ({score})")
        ui.dsmLevelTwoSomaticSymptomNextButton.setEnabled(True)

    def go_next():
        nonlocal current_idx
        current_idx += 1
        if current_idx >= len(questions):
            show_submit()
        else:
            show_question(current_idx)

    def show_submit():
        # Clear all UI
        ui.dsmLevelTwoSomaticSymptomLabel.setText("All done! Click Submit to save your results.")
        while ui.dsmLevelTwoSomaticSymptomQuestionLayout.count():
            item = ui.dsmLevelTwoSomaticSymptomQuestionLayout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
        ui.dsmLevelTwoSomaticSymptomNextButton.setVisible(False)

        submit_btn = QPushButton("Submit")
        submit_btn.setMinimumHeight(50)
        submit_btn.setStyleSheet("background-color: green; color: white; font-size: 18px;")
        submit_btn.clicked.connect(submit)
        ui.dsmLevelTwoSomaticSymptomQuestionLayout.addWidget(submit_btn)
        print("[DEBUG] All cleared — Submit button shown!")

    def submit():
        total_raw = sum(selected_scores.values())
        print(f"[RESULT] Raw Total: {total_raw}")

        # Prorated for children, not for adults
        if is_adult:
            prorated_score = total_raw
            score_type = "PHQ-15 Score"
        else:
            prorated_score = round(total_raw * 15 / 13)
            score_type = "Prorated Score"

        # Severity Interpretation Table
        if 0 <= prorated_score <= 4:
            severity = "Minimal"
        elif 5 <= prorated_score <= 9:
            severity = "Low"
            sendNotification("Low Somatic Symptoms Detected")
            sendLog("Low Somatic Sypmtoms Detected")
        elif 10 <= prorated_score <= 14:
            severity = "Medium"
            sendNotification("Medium Somatic Symptoms Detected")
            sendLog("Medium Somatic Symptoms Detected")
        elif 15 <= prorated_score <= 30:
            severity = "High"
            sendNotification("High Somatic Symptoms Detected")
            sendLog("High Somatic Symptoms Detected")
        else:
            severity = "Unknown"

        print(f"[RESULT] {score_type}: {prorated_score} — Severity: {severity}")

        # Save results
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        result_key = f"dsm_level_two_somatic_symptom_{timestamp}"

        results = {
            "questions": {
                f"Q{q + 1}": selected_answers[q] for q in selected_answers
            },
            "total_raw_score": total_raw,
            "prorated_score" if not is_adult else "phq_15_score": prorated_score,
            "severity": severity
        }

        results_dir = f"TomoBrain/Data/Users/{username}/Results"
        os.makedirs(results_dir, exist_ok=True)

        results_file = os.path.join(results_dir, "dsm_level_two_somatic_symptom_results.json")
        all_results = {}

        if os.path.exists(results_file):
            with open(results_file, "r") as f:
                try:
                    all_results = json.load(f)
                except Exception:
                    all_results = {}

        all_results[result_key] = results

        with open(results_file, "w") as f:
            json.dump(all_results, f, indent=4)

        print(f"[INFO] Saved results to: {results_file}")
        ui.stackedWidget.setCurrentWidget(ui.Dashboard)

    ui.dsmLevelTwoSomaticSymptomNextButton.setEnabled(False)
    ui.dsmLevelTwoSomaticSymptomNextButton.setText("Next")
    ui.dsmLevelTwoSomaticSymptomNextButton.setVisible(True)
    ui.dsmLevelTwoSomaticSymptomNextButton.clicked.connect(go_next)

    show_question(current_idx)




def run_dsm_level_two_anxiety(ui):
    """
    Runs DSM Level Two Anxiety Test on a single page.
    Saves results under Results folder per user.
    """

    selected_scores = {}
    selected_answers = {}
    current_idx = 0
    answer_buttons = []

    # ✅ Load user age + username
    with open("TomoBrain/Data/Users/current_user.json") as f:
        user_data = json.load(f)
    age = int(user_data["age"])
    username = user_data.get("username", "unknown")

    is_adult = age >= 18
    sheet = "Adult" if is_adult else "Child"
    ui.dsmLevelTwoAnxietyTitleLabel.setText(f"DSM Level Two Anxiety — {'Adult' if is_adult else 'Child'}")

    print(f"[DEBUG] User age: {age} — Using sheet: {sheet}")

    # ✅ Load questions (no header!)
    df = pd.read_excel(
        "TomoBrain/Data/Tests/dsm_level_two_anxiety.xlsx",
        sheet_name=sheet,
        header=None
    )
    questions = df[0].dropna().tolist()
    print(f"[DEBUG] Loaded {len(questions)} questions")

    def show_question(idx):
        nonlocal answer_buttons
        ui.dsmLevelTwoAnxietyNextButton.setEnabled(False)
        ui.dsmLevelTwoAnxietyNextButton.setVisible(True)
        answer_buttons = []

        if idx >= len(questions):
            show_submit()
            return

        question = questions[idx]
        ui.dsmLevelTwoAnxietyLabel.setText(question)

        print(f"[DEBUG] Q{idx + 1}: {question}")

        while ui.dsmLevelTwoAnxietyQuestionLayout.count():
            item = ui.dsmLevelTwoAnxietyQuestionLayout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        labels = [
            ("Never", 1),
            ("Rarely", 2),
            ("Sometimes", 3),
            ("Often", 4),
            ("Always", 5)
        ]

        for text, score in labels:
            btn = QPushButton(text)
            btn.setStyleSheet("background-color: white; color: black; font-size:24px;")
            btn.clicked.connect(lambda _, s=score, t=text, b=btn: handle_answer(s, t, b, idx))
            ui.dsmLevelTwoAnxietyQuestionLayout.addWidget(btn)
            answer_buttons.append(btn)

    def handle_answer(score, answer_text, clicked_button, q_idx):
        selected_scores[q_idx] = score
        selected_answers[q_idx] = {"answer_text": answer_text, "score": score}

        for btn in answer_buttons:
            btn.setStyleSheet("background-color: white; color: black;")
        clicked_button.setStyleSheet("background-color: #008060; color: white;")

        print(f"[DEBUG] Q{q_idx + 1} | {answer_text} ({score})")
        ui.dsmLevelTwoAnxietyNextButton.setEnabled(True)

    def go_next():
        nonlocal current_idx
        current_idx += 1
        # Only show submit after last question
        if current_idx >= len(questions):
            show_submit()
        else:
            show_question(current_idx)

    def show_submit():
        ui.dsmLevelTwoAnxietyLabel.setText("All done! Click Submit to save your results.")

        while ui.dsmLevelTwoAnxietyQuestionLayout.count():
            item = ui.dsmLevelTwoAnxietyQuestionLayout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        ui.dsmLevelTwoAnxietyNextButton.setVisible(False)

        submit_btn = QPushButton("Submit")
        submit_btn.setMinimumHeight(50)
        submit_btn.setStyleSheet("background-color: green; color: white; font-size: 18px;")
        submit_btn.clicked.connect(submit)
        ui.dsmLevelTwoAnxietyQuestionLayout.addWidget(submit_btn)

        print("[DEBUG] Submit button shown!")

    def submit():
        total_raw = sum(selected_scores.values())
        print(f"[RESULT] Raw Total: {total_raw}")

        if not is_adult:
            tscore_map = {
                13: 32.3, 14: 36.6, 15: 38.9, 16: 41.1, 17: 42.8, 18: 44.3, 19: 45.7, 20: 47, 21: 48.2,
                22: 49.4, 23: 50.4, 24: 51.4, 25: 52.4, 26: 53.3, 27: 54.2, 28: 55.1, 29: 56, 30: 56.8,
                31: 57.6, 32: 58.4, 33: 59.2, 34: 60, 35: 60.8, 36: 61.6, 37: 62.3, 38: 63.1, 39: 63.8,
                40: 64.5, 41: 65.3, 42: 66, 43: 66.8, 44: 67.5, 45: 68.2, 46: 69, 47: 69.7, 48: 70.5,
                49: 71.3, 50: 72, 51: 72.8, 52: 73.6, 53: 74.4, 54: 75.3, 55: 76.1, 56: 77, 57: 77.9,
                58: 78.9, 59: 79.9, 60: 81, 61: 82.1, 62: 83.3, 63: 84.7, 64: 86.1, 65: 88
            }
        else:
            tscore_map = {
                7: 36.3, 8: 42.1, 9: 44.7, 10: 46.7, 11: 48.4, 12: 49.9, 13: 51.3, 14: 52.6, 15: 53.8,
                16: 55.1, 17: 56.3, 18: 57.6, 19: 58.8, 20: 60, 21: 61.3, 22: 62.6, 23: 63.8, 24: 65.1,
                25: 66.4, 26: 67.7, 27: 68.9, 28: 70.2, 29: 71.5, 30: 72.9, 31: 74.3, 32: 75.8, 33: 77.4,
                34: 79.5, 35: 82.7
            }

        tscore = tscore_map.get(total_raw, "N/A")
        severity = "Unknown"
        if isinstance(tscore, (int, float)):
            if tscore < 55:
                severity = "None to slight"
            elif 55 <= tscore < 60:
                severity = "Mild"
                sendNotification("Possible MILD Anxiety Detected.")
                sendLog("Mild Anxiety Detected")
            elif 60 <= tscore < 70:
                severity = "Moderate"
                sendNotification("Possible MODERATE Anxiety Detected.")
                sendLog("Moderate Anxiety Detected")
            elif tscore >= 70:
                severity = "Severe"
                sendNotification("Possible SEVERE Anxiety Detected.")
                sendLog("Severe Anxiety Detected")

        print(f"[RESULT] Raw: {total_raw} => T-Score: {tscore} => Severity: {severity}")

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        result_key = f"dsm_level_two_anxiety_{timestamp}"

        results = {
            "questions": {
                f"Q{q + 1}": selected_answers[q] for q in selected_answers
            },
            "total_raw_score": total_raw,
            "tscore": tscore,
            "severity": severity
        }

        results_dir = f"TomoBrain/Data/Users/{username}/Results"
        os.makedirs(results_dir, exist_ok=True)

        results_file = os.path.join(results_dir, "dsm_level_two_anxiety_results.json")
        all_results = {}

        if os.path.exists(results_file):
            with open(results_file, "r") as f:
                try:
                    all_results = json.load(f)
                except Exception:
                    all_results = {}

        all_results[result_key] = results

        with open(results_file, "w") as f:
            json.dump(all_results, f, indent=4)

        print(f"[INFO] Saved results to: {results_file}")

        ui.stackedWidget.setCurrentWidget(ui.Dashboard)

    # Always show the next button and set up handlers for both adults and children
    ui.dsmLevelTwoAnxietyNextButton.setEnabled(False)
    ui.dsmLevelTwoAnxietyNextButton.setText("Next")
    ui.dsmLevelTwoAnxietyNextButton.setVisible(True)
    ui.dsmLevelTwoAnxietyNextButton.clicked.connect(go_next)

    show_question(current_idx)


def sendLog(msg):
    """
    Loads current_user.json to get username,
    then appends {timestamp: msg} to user_logs.json as a dictionary.
    """

    current_user_file = "TomoBrain/Data/Users/current_user.json"
    if not os.path.exists(current_user_file):
        print("[ERROR] current_user.json not found!")
        return

    with open(current_user_file, "r") as f:
        user_data = json.load(f)

    username = user_data.get("username")
    if not username:
        print("[ERROR] Username missing in current_user.json!")
        return

    # ✅ Ensure Logs folder exists
    logs_dir = f"TomoBrain/Data/Users/{username}/Logs"
    os.makedirs(logs_dir, exist_ok=True)

    log_file = os.path.join(logs_dir, "user_logs.json")

    logs = {}
    if os.path.exists(log_file):
        with open(log_file, "r") as f:
            try:
                logs = json.load(f)
                if not isinstance(logs, dict):
                    print("[WARN] user_logs.json is not a dict — resetting.")
                    logs = {}
            except Exception:
                logs = {}

    # ✅ Add new entry with timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logs[timestamp] = msg

    with open(log_file, "w") as f:
        json.dump(logs, f, indent=4)

    print(f"[INFO] Log added for {username}: [{timestamp}] {msg}")



def sendNotification(msg):
    """
    Loads current_user.json to get username,
    then appends `msg` to their notifications.json IF it isn't already present.
    """
    current_user_file = "TomoBrain/Data/Users/current_user.json"
    if not os.path.exists(current_user_file):
        print("[ERROR] current_user.json not found!")
        return

    with open(current_user_file, "r") as f:
        user_data = json.load(f)

    username = user_data.get("username")
    if not username:
        print("[ERROR] Username missing in current_user.json!")
        return

    notif_file = f"TomoBrain/Data/Users/{username}/notifications.json"
    notifications = []
    if os.path.exists(notif_file):
        with open(notif_file, "r") as f:
            try:
                notifications = json.load(f)
                if not isinstance(notifications, list):
                    print("[WARN] notifications.json is not a list, resetting.")
                    notifications = []
            except Exception:
                notifications = []

    if msg in notifications:
        print(f"[INFO] Notification already exists for {username}: {msg}")
        return

    notifications.append(msg)
    with open(notif_file, "w") as f:
        json.dump(notifications, f, indent=4)

    print(f"[INFO] Added notification for {username}: {msg}")



def run_dsm_level_one_test(ui):
    """
    Runs DSM Level One flow on a single page, and saves results per user.
    """
    import os
    import json
    from datetime import datetime
    from collections import defaultdict
    from PySide6.QtWidgets import QPushButton

    selected_scores = {}
    selected_answers = {}
    domain_totals = defaultdict(int)
    current_idx = 0
    answer_buttons = []

    # === Load user age + username ===
    with open("TomoBrain/Data/Users/current_user.json") as f:
        user_data = json.load(f)
    age = int(user_data["age"])
    username = user_data.get("username", "unknown")

    is_adult = age >= 18
    sheet = "Adult" if is_adult else "Child"
    ui.dsmLevelOneTitleLabel.setText(f"DSM Level One - {'Adult' if is_adult else 'Child'}")

    print(f"[DEBUG] User age: {age} — Using sheet: {sheet}")

    df = pd.read_excel("TomoBrain/Data/Tests/DSM Cut Corners Level One.xlsx", sheet_name=sheet)
    questions = df["Question"].dropna().tolist()
    print(f"[DEBUG] Loaded {len(questions)} questions")

    def get_domain(q_idx):
        if is_adult:
            if q_idx in [0, 1]: return "Depression"
            if q_idx == 2: return "Anger"
            if q_idx in [3, 4]: return "Mania"
            if q_idx in [5, 6, 7]: return "Anxiety"
            if q_idx in [8, 9]: return "Somatic Symptoms"
            if q_idx == 10: return "Suicidal Ideation"
            if q_idx in [11, 12]: return "Psychosis"
            if q_idx == 13: return "Sleep Problems"
            if q_idx == 14: return "Memory"
            if q_idx in [15, 16]: return "Repetitive Thoughts/Behaviors"
            if q_idx in [17, 18, 19]: return "Dissociation/Personality Functioning"
            if q_idx in [20, 21, 22]: return "Substance Use"
        else:
            if q_idx in [0, 1]: return "Somatic Symptoms"
            if q_idx == 2: return "Sleep Problems"
            if q_idx == 3: return "Inattention"
            if q_idx in [4, 5]: return "Depression"
            if q_idx in [6, 7]: return "Anger/Irritability"
            if q_idx in [8, 9]: return "Mania"
            if q_idx in [10, 11, 12]: return "Anxiety"
            if q_idx in [13, 14]: return "Psychosis"
            if q_idx in [15, 16, 17, 18]: return "Repetitive Thoughts/Behaviors"
            if q_idx in [19, 20, 21, 22]: return "Substance Use"
            if q_idx in [23, 24]: return "Suicidal Ideation"
        return "Unknown"

    def show_question(idx):
        nonlocal answer_buttons
        ui.dsmLevelOneNext.setEnabled(False)
        ui.dsmLevelOneNext.setVisible(True)  # Always show Next unless on submit
        answer_buttons = []

        if idx >= len(questions):
            show_submit()
            return

        question = questions[idx]
        ui.dsmLevelOneLabel.setText(question)

        print(f"[DEBUG] Q{idx + 1}: {question} — Domain: {get_domain(idx)}")

        while ui.dsmLevelOneQuestionLayout.count():
            item = ui.dsmLevelOneQuestionLayout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        # === Determine labels ===
        if is_adult:
            labels = [
                ("None — Not at all", 0),
                ("Slight — Rare, less than a day or two", 1),
                ("Mild — Several days", 2),
                ("Moderate — More than half the days", 3),
                ("Severe — Nearly every day", 4)
            ]
        else:
            if idx >= 19:  # Child Q20–25 → Yes/No
                labels = [("No", 0), ("Yes", 1)]
            else:
                labels = [
                    ("None — Not at all", 0),
                    ("Slight — Rare, less than a day or two", 1),
                    ("Mild — Several days", 2),
                    ("Moderate — More than half the days", 3),
                    ("Severe — Nearly every day", 4)
                ]

        for text, score in labels:
            btn = QPushButton(text)
            btn.setStyleSheet("background-color: white; color: black; font-size: 24px;")
            btn.clicked.connect(lambda _, s=score, t=text, b=btn: handle_answer(s, t, b, idx))
            ui.dsmLevelOneQuestionLayout.addWidget(btn)
            answer_buttons.append(btn)

    def handle_answer(score, answer_text, clicked_button, q_idx):
        selected_scores[q_idx] = score
        selected_answers[q_idx] = {
            "question": questions[q_idx] if q_idx < len(questions) else f"Q{q_idx+1}",
            "answer": answer_text,
            "score": score,
            "domain": get_domain(q_idx)
        }
        for btn in answer_buttons:
            btn.setStyleSheet("background-color: white; color: black;")
        clicked_button.setStyleSheet("background-color: #008060; color: white;")

        domain = get_domain(q_idx)
        domain_totals[domain] += score

        print(f"[DEBUG] Q{q_idx + 1} | Answer: {score} | Domain: {domain} | Total: {domain_totals[domain]}")

        ui.dsmLevelOneNext.setEnabled(True)

    def go_next():
        nonlocal current_idx
        current_idx += 1
        if current_idx >= len(questions):
            show_submit()
        else:
            show_question(current_idx)

    def show_submit():
        # ✅ Clear all UI
        ui.dsmLevelOneLabel.setText("")
        while ui.dsmLevelOneQuestionLayout.count():
            item = ui.dsmLevelOneQuestionLayout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        ui.dsmLevelOneNext.setVisible(False)

        # ✅ Add big Submit
        submit_btn = QPushButton("Submit")
        submit_btn.setMinimumHeight(50)
        submit_btn.setStyleSheet("background-color: green; color: white; font-size: 18px;")
        submit_btn.clicked.connect(submit)
        ui.dsmLevelOneQuestionLayout.addWidget(submit_btn)

        print("[DEBUG] All cleared — Submit button shown!")

    def submit():
        print("\n=== [FINAL RESULTS] ===")
        for q_idx, score in selected_scores.items():
            print(f"Q{q_idx + 1}: {score} => {get_domain(q_idx)}")
            if score >= 2 and get_domain(q_idx) == "Depression":
                sendNotification("Take DSM Level Two - Depression")
            if score >= 2 and get_domain(q_idx) == "Anger":
                sendNotification("Take DSM Level Two - Anger")
            if score >= 2 and get_domain(q_idx) == "Mania":
                sendNotification("Take DSM Level Two - Mania")
            if score >= 2 and get_domain(q_idx) == "Anger/Irritability":
                sendNotification("Take DSM Level Two - Anger")
                sendNotification("Take DSM Level Two - Irritability")
            if score >= 2 and get_domain(q_idx) == "Anxiety":
                sendNotification("Take DSM Level Two - Anxiety")
            if score >= 2 and get_domain(q_idx) == "Somatic Symptoms":
                sendNotification("Take DSM Level Two - Somatic Symptoms")
            if score >= 2 and get_domain(q_idx) == "Sleep Problems":
                sendNotification("Take DSM Level Two - Sleep Disturbance")
            if score >= 2 and get_domain(q_idx) == "Repetitive Thoughts/Behaviors":
                sendNotification("Take DSM Level Two - Repetitive Thoughts & Behaviors")
            if (score >= 2 and get_domain(q_idx) == "Substance Use") or (score >= 1 and get_domain(q_idx) == "Substance Use" and not is_adult):
                sendNotification("Take DSM Level Two - Substance Use")
        print(f"Domain totals: {dict(domain_totals)}")

        # === SAVE RESULTS TO FILE (new!) ===
        results = {
            "questions": selected_answers,
            "domain_totals": dict(domain_totals),
            "total_raw_score": sum(selected_scores.values()),
            "age": age,
            "is_adult": is_adult,
            "timestamp": datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        }
        # Save to user's Results folder
        results_dir = f"TomoBrain/Data/Users/{username}/Results"
        os.makedirs(results_dir, exist_ok=True)
        results_file = os.path.join(results_dir, "dsm_level_one_results.json")
        all_results = {}
        if os.path.exists(results_file):
            with open(results_file, "r") as f:
                try:
                    all_results = json.load(f)
                except Exception:
                    all_results = {}
        key = f"dsm_level_one_{results['timestamp']}"
        all_results[key] = results
        with open(results_file, "w") as f:
            json.dump(all_results, f, indent=4)

        print(f"[INFO] Saved DSM Level One results to: {results_file}")

        ui.stackedWidget.setCurrentWidget(ui.Dashboard)

    ui.dsmLevelOneNext.setEnabled(False)
    ui.dsmLevelOneNext.setText("Next")
    ui.dsmLevelOneNext.setVisible(True)
    ui.dsmLevelOneNext.clicked.connect(go_next)

    show_question(current_idx)



def run_dsm_level_two_depression(ui):
    """
    Runs DSM Level Two Depression Test on a single page.
    Saves results under Results folder per user.
    """

    import os
    import json
    from datetime import datetime
    import pandas as pd
    from PySide6.QtWidgets import QPushButton

    selected_scores = {}
    selected_answers = {}
    current_idx = 0
    answer_buttons = []

    # ✅ Load user age + username
    with open("TomoBrain/Data/Users/current_user.json") as f:
        user_data = json.load(f)
    age = int(user_data["age"])
    username = user_data.get("username", "unknown")

    is_adult = age >= 18
    sheet = "Adult" if is_adult else "Child"
    ui.dsmLevelTwoDepressionTitleLabel.setText(f"DSM Level Two Depression — {'Adult' if is_adult else 'Child'}")

    print(f"[DEBUG] User age: {age} — Using sheet: {sheet}")

    # ✅ Load questions (no header!)
    df = pd.read_excel(
        "TomoBrain/Data/Tests/dsm_level_two_depression.xlsx",
        sheet_name=sheet,
        header=None
    )
    questions = df[0].dropna().tolist()
    print(f"[DEBUG] Loaded {len(questions)} questions")

    def show_question(idx):
        nonlocal answer_buttons
        ui.dsmLevelTwoDepressionNextButton.setEnabled(False)
        ui.dsmLevelTwoDepressionNextButton.setVisible(True)
        answer_buttons = []

        if idx >= len(questions):
            show_submit()
            return

        question = questions[idx]
        ui.dsmLevelTwoDepressionLabel.setText(question)

        print(f"[DEBUG] Q{idx + 1}: {question}")

        while ui.dsmLevelTwoDepressionQuestionLayout.count():
            item = ui.dsmLevelTwoDepressionQuestionLayout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        labels = [
            ("Never", 1),
            ("Rarely", 2),
            ("Sometimes", 3),
            ("Often", 4),
            ("Always", 5)
        ]

        for text, score in labels:
            btn = QPushButton(text)
            btn.setStyleSheet("background-color: white; color: black; font-size:24px;")
            btn.clicked.connect(lambda _, s=score, t=text, b=btn: handle_answer(s, t, b, idx))
            ui.dsmLevelTwoDepressionQuestionLayout.addWidget(btn)
            answer_buttons.append(btn)

    def handle_answer(score, answer_text, clicked_button, q_idx):
        selected_scores[q_idx] = score
        selected_answers[q_idx] = {"answer_text": answer_text, "score": score}

        for btn in answer_buttons:
            btn.setStyleSheet("background-color: white; color: black;")
        clicked_button.setStyleSheet("background-color: #008060; color: white;")

        print(f"[DEBUG] Q{q_idx + 1} | {answer_text} ({score})")
        ui.dsmLevelTwoDepressionNextButton.setEnabled(True)

    def go_next():
        nonlocal current_idx
        current_idx += 1
        show_question(current_idx)

    def show_submit():
        # --- Clear the layout and hide Next, add big Submit button like DSM Level One ---
        ui.dsmLevelTwoDepressionLabel.setText("All done! Click Submit to save your results.")
        while ui.dsmLevelTwoDepressionQuestionLayout.count():
            item = ui.dsmLevelTwoDepressionQuestionLayout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
        ui.dsmLevelTwoDepressionNextButton.setVisible(False)

        submit_btn = QPushButton("Submit")
        submit_btn.setMinimumHeight(50)
        submit_btn.setStyleSheet("background-color: green; color: white; font-size: 18px;")
        submit_btn.clicked.connect(submit)
        ui.dsmLevelTwoDepressionQuestionLayout.addWidget(submit_btn)
        print("[DEBUG] Submit button added!")

    def submit():
        total_raw = sum(selected_scores.values())
        print(f"[RESULT] Raw Total: {total_raw}")

        if is_adult:
            tscore_map = {
                8: 37.1, 9: 43.3, 10: 46.2, 11: 48.2, 12: 49.8,
                13: 51.2, 14: 52.3, 15: 53.4, 16: 54.3, 17: 55.3,
                18: 56.2, 19: 57.1, 20: 57.9, 21: 58.8, 22: 59.7,
                23: 60.7, 24: 61.6, 25: 62.5, 26: 63.5, 27: 64.4,
                28: 65.4, 29: 66.4, 30: 67.4, 31: 68.3, 32: 69.3,
                33: 70.4, 34: 71.4, 35: 72.5, 36: 73.6, 37: 74.8,
                38: 76.2, 39: 77.9, 40: 81.1
            }
        else:
            tscore_map = {
                14: 31.7, 15: 35.2, 16: 36.9, 17: 39.1, 18: 40.6,
                19: 42.4, 20: 43.8, 21: 45.2, 22: 46.5, 23: 47.6,
                24: 48.7, 25: 49.7, 26: 50.6, 27: 51.5, 28: 52.4,
                29: 53.2, 30: 54.0, 31: 54.8, 32: 55.7, 33: 56.3,
                34: 57.0, 35: 57.7, 36: 58.4, 37: 59.1, 38: 59.8,
                39: 60.4, 40: 61.1, 41: 61.8, 42: 62.4, 43: 63.1,
                44: 63.8, 45: 64.4, 46: 65.1, 47: 65.7, 48: 66.4,
                49: 67.0, 50: 67.7, 51: 68.4, 52: 69.0, 53: 69.7,
                54: 70.4, 55: 71.1, 56: 71.8, 57: 72.6, 58: 73.3,
                59: 74.1, 60: 74.9, 61: 75.7, 62: 76.6, 63: 77.5,
                64: 78.4, 65: 79.4, 66: 80.6, 67: 81.7, 68: 83.1,
                69: 84.6, 70: 86.6
            }

        tscore = tscore_map.get(total_raw, "N/A")

        severity = "Unknown"
        if isinstance(tscore, (int, float)):
            if tscore < 55:
                severity = "None to slight"
            elif 55 <= tscore < 60:
                severity = "Mild"
                sendNotification("Possible MILD Depression Detected.")
                sendLog("Mild Depression Detected")
            elif 60 <= tscore < 70:
                severity = "Moderate"
                sendNotification("Possible MODERATE Depression Detected.")
                sendLog("Moderate Depression Detected")
            elif tscore >= 70:
                severity = "Severe"
                sendNotification("Possible SEVERE Depression Detected")
                sendLog("Severe Depression Detected")
        print(f"[RESULT] Raw: {total_raw} => T-Score: {tscore} => Severity: {severity}")

        # ✅ Prepare results dictionary
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        result_key = f"dsm_level_two_depression_{timestamp}"

        results = {
            "questions": {
                f"Q{q + 1}": selected_answers[q] for q in selected_answers
            },
            "total_raw_score": total_raw,
            "tscore": tscore,
            "severity": severity
        }

        # ✅ Write to file in user Results folder
        results_dir = f"TomoBrain/Data/Users/{username}/Results"
        os.makedirs(results_dir, exist_ok=True)

        results_file = os.path.join(results_dir, "dsm_level_two_depression_results.json")

        all_results = {}
        if os.path.exists(results_file):
            with open(results_file, "r") as f:
                try:
                    all_results = json.load(f)
                except Exception:
                    all_results = {}

        all_results[result_key] = results

        with open(results_file, "w") as f:
            json.dump(all_results, f, indent=4)

        print(f"[INFO] Saved results to: {results_file}")

        ui.stackedWidget.setCurrentWidget(ui.Dashboard)

    ui.dsmLevelTwoDepressionNextButton.setEnabled(False)
    ui.dsmLevelTwoDepressionNextButton.setText("Next")
    ui.dsmLevelTwoDepressionNextButton.setVisible(True)
    ui.dsmLevelTwoDepressionNextButton.clicked.connect(go_next)

    show_question(current_idx)



def run_dsm_level_two_anger(ui):
    """
    Runs DSM Level Two Anger Test on a single page.
    Saves results under Results folder per user.
    """

    selected_scores = {}
    selected_answers = {}
    current_idx = 0
    answer_buttons = []

    # ✅ Load user age + username
    with open("TomoBrain/Data/Users/current_user.json") as f:
        user_data = json.load(f)
    age = int(user_data["age"])
    username = user_data.get("username", "unknown")

    is_adult = age >= 18
    sheet = "Adult" if is_adult else "Child"
    ui.dsmLevelTwoAngerTitleLabel.setText(f"DSM Level Two Anger — {'Adult' if is_adult else 'Child'}")

    print(f"[DEBUG] User age: {age} — Using sheet: {sheet}")

    # ✅ Load questions (no header!)
    df = pd.read_excel(
        "TomoBrain/Data/Tests/dsm_level_two_anger.xlsx",
        sheet_name=sheet,
        header=None
    )
    questions = df[0].dropna().tolist()
    print(f"[DEBUG] Loaded {len(questions)} questions")

    def show_question(idx):
        nonlocal answer_buttons
        ui.dsmLevelTwoAngerNextButton.setEnabled(False)
        answer_buttons = []

        if idx >= len(questions):
            show_submit()
            return

        question = questions[idx]
        ui.dsmLevelTwoAngerLabel.setText(question)

        print(f"[DEBUG] Q{idx + 1}: {question}")

        while ui.dsmLevelTwoAngerQuestionLayout.count():
            item = ui.dsmLevelTwoAngerQuestionLayout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        labels = [
            ("Never", 1),
            ("Rarely", 2),
            ("Sometimes", 3),
            ("Often", 4),
            ("Always", 5)
        ]

        for text, score in labels:
            btn = QPushButton(text)
            btn.setStyleSheet("background-color: white; color: black; font-size:20px;")
            btn.clicked.connect(lambda _, s=score, t=text, b=btn: handle_answer(s, t, b, idx))
            ui.dsmLevelTwoAngerQuestionLayout.addWidget(btn)
            answer_buttons.append(btn)

    def handle_answer(score, answer_text, clicked_button, q_idx):
        selected_scores[q_idx] = score
        selected_answers[q_idx] = {"answer_text": answer_text, "score": score}

        for btn in answer_buttons:
            btn.setStyleSheet("background-color: white; color: black;")
        clicked_button.setStyleSheet("background-color: #008060; color: white;")

        print(f"[DEBUG] Q{q_idx + 1} | {answer_text} ({score})")
        ui.dsmLevelTwoAngerNextButton.setEnabled(True)

    def go_next():
        nonlocal current_idx
        current_idx += 1
        show_question(current_idx)

    def show_submit():
        # ✅ Clear question text and answers
        ui.dsmLevelTwoAngerLabel.setText("All done! Click Submit to save your results.")

        while ui.dsmLevelTwoAngerQuestionLayout.count():
            item = ui.dsmLevelTwoAngerQuestionLayout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        ui.dsmLevelTwoAngerNextButton.setVisible(False)

        submit_btn = QPushButton("Submit")
        submit_btn.setMinimumHeight(50)
        submit_btn.setStyleSheet("background-color: green; color: white; font-size: 18px;")
        submit_btn.clicked.connect(submit)
        ui.dsmLevelTwoAngerQuestionLayout.addWidget(submit_btn)
        print("[DEBUG] Submit button added!")

    def submit():
        total_raw = sum(selected_scores.values())
        print(f"[RESULT] Raw Total: {total_raw}")

        if is_adult:
            tscore_map = {
                6: 31.1, 7: 35.9, 8: 39, 9: 41.7, 10: 44.2,
                11: 46.4, 12: 48.5, 13: 50.5, 14: 52.4, 15: 54.2,
                16: 56.0, 17: 57.7, 18: 59.5, 19: 61.2, 20: 62.9,
                21: 64.6, 22: 66.3, 23: 68.0, 24: 69.8, 25: 71.6,
                26: 73.4, 27: 75.4, 28: 77.5, 29: 79.8, 30: 82.7
            }
        else:
            tscore_map = {
                6: 31.1, 7: 35.9, 8: 39.0, 9: 41.7, 10: 44.2,
                11: 46.4, 12: 48.5, 13: 50.5, 14: 52.4, 15: 54.2,
                16: 55.0, 17: 57.7, 18: 59.5, 19: 61.2, 20: 62.9,
                21: 64.6, 22: 66.3, 23: 68.0, 24: 69.8, 25: 71.6,
                26: 73.4, 27:75.4, 28:77.5, 29:79.8, 30:82.7
            }

        tscore = tscore_map.get(total_raw, "N/A")

        severity = "Unknown"
        if isinstance(tscore, (int, float)):
            if tscore < 55:
                severity = "None to slight"
            elif 55 <= tscore < 60:
                severity = "Mild"
                sendNotification("Possible MILD Anger Issue Detected.")
                sendLog("Mild Anger Issue Detected")
            elif 60 <= tscore < 70:
                severity = "Moderate"
                sendNotification("Possible MODERATE Anger Issue Detected.")
                sendLog("Moderate Anger Issue Detected")
            elif tscore >= 70:
                severity = "Severe"
                sendNotification("Possible SEVERE Anger Issue Detected.")
                sendLog("Severe Anger Issue Detected")

        print(f"[RESULT] Raw: {total_raw} => T-Score: {tscore} => Severity: {severity}")

        # ✅ Save results
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        result_key = f"dsm_level_two_anger_{timestamp}"

        results = {
            "questions": {
                f"Q{q + 1}": selected_answers[q] for q in selected_answers
            },
            "total_raw_score": total_raw,
            "tscore": tscore,
            "severity": severity
        }

        results_dir = f"TomoBrain/Data/Users/{username}/Results"
        os.makedirs(results_dir, exist_ok=True)

        results_file = os.path.join(results_dir, "dsm_level_two_anger_results.json")
        all_results = {}

        if os.path.exists(results_file):
            with open(results_file, "r") as f:
                try:
                    all_results = json.load(f)
                except Exception:
                    all_results = {}

        all_results[result_key] = results

        with open(results_file, "w") as f:
            json.dump(all_results, f, indent=4)

        print(f"[INFO] Saved results to: {results_file}")

        ui.stackedWidget.setCurrentWidget(ui.Dashboard)

    ui.dsmLevelTwoAngerNextButton.setEnabled(False)
    ui.dsmLevelTwoAngerNextButton.setText("Next")
    ui.dsmLevelTwoAngerNextButton.clicked.connect(go_next)

    show_question(current_idx)



def run_dsm_level_two_mania(ui):
    """
    Runs DSM Level Two Mania Test on a single page.
    Saves results under Results folder per user.
    """

    selected_scores = {}
    selected_answers = {}
    current_idx = 0
    answer_buttons = []

    # ✅ Load user age + username
    with open("TomoBrain/Data/Users/current_user.json") as f:
        user_data = json.load(f)
    age = int(user_data["age"])
    username = user_data.get("username", "unknown")

    is_adult = age >= 18
    sheet = "Adult" if is_adult else "Child"
    ui.dsmLevelTwoManiaTitleLabel.setText(f"DSM Level Two Mania — {'Adult' if is_adult else 'Child'}")

    print(f"[DEBUG] User age: {age} — Using sheet: {sheet}")

    # ✅ Load questions (no header!)
    df = pd.read_excel(
        "TomoBrain/Data/Tests/dsm_level_two_mania.xlsx",
        sheet_name=sheet,
        header=None
    )
    questions = df[0].dropna().tolist()
    print(f"[DEBUG] Loaded {len(questions)} questions")

    # === Answer text per question ===
    answer_texts = [
        [
            "I do not feel happier or more cheerful than usual.",
            "I occasionally feel happier or more cheerful than usual.",
            "I often feel happier or more cheerful than usual.",
            "I feel happier or more cheerful than usual most of the time.",
            "I feel happier or more cheerful than usual all of the time."
        ],
        [
            "I do not feel more self-confident than usual.",
            "I occasionally feel more self-confident than usual.",
            "I often feel more self-confident than usual.",
            "I frequently feel more self-confident than usual.",
            "I feel extremely self-confident all of the time."
        ],
        [
            "I do not need less sleep than usual.",
            "I occasionally need less sleep than usual.",
            "I often need less sleep than usual.",
            "I frequently need less sleep than usual.",
            "I can go all day and all night without any sleep and still not feel tired."
        ],
        [
            "I do not talk more than usual.",
            "I occasionally talk more than usual.",
            "I often talk more than usual.",
            "I frequently talk more than usual.",
            "I talk constantly and cannot be interrupted."
        ],
        [
            "I have not been more active than usual (either socially, sexually, at work, home, or school).",
            "I have occasionally been more active than usual.",
            "I have often been more active than usual.",
            "I have frequently been more active than usual.",
            "I am constantly more active or on the go all the time."
        ]
    ]

    def show_question(idx):
        nonlocal answer_buttons
        ui.dsmLevelTwoManiaNextButton.setEnabled(False)
        answer_buttons = []

        if idx >= len(questions):
            show_submit()
            return

        question = questions[idx]
        ui.dsmLevelTwoManiaLabel.setText(question)

        print(f"[DEBUG] Q{idx + 1}: {question}")

        while ui.dsmLevelTwoManiaQuestionLayout.count():
            item = ui.dsmLevelTwoManiaQuestionLayout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        labels = answer_texts[idx]

        for score, text in enumerate(labels):
            btn = QPushButton(text)
            btn.setStyleSheet("background-color: white; color: black; font-size:24px;")
            btn.clicked.connect(lambda _, s=score, t=text, b=btn: handle_answer(s, t, b, idx))
            ui.dsmLevelTwoManiaQuestionLayout.addWidget(btn)
            answer_buttons.append(btn)

    def handle_answer(score, answer_text, clicked_button, q_idx):
        selected_scores[q_idx] = score
        selected_answers[q_idx] = {"answer_text": answer_text, "score": score}

        for btn in answer_buttons:
            btn.setStyleSheet("background-color: white; color: black;")
        clicked_button.setStyleSheet("background-color: #008060; color: white;")

        print(f"[DEBUG] Q{q_idx + 1} | {answer_text} ({score})")
        ui.dsmLevelTwoManiaNextButton.setEnabled(True)

    def go_next():
        nonlocal current_idx
        current_idx += 1
        show_question(current_idx)

    def show_submit():
        # === Only change: clear all UI, hide Next, show big Submit ===
        ui.dsmLevelTwoManiaLabel.setText("All done! Click Submit to save your results.")

        # Clear buttons/layout
        while ui.dsmLevelTwoManiaQuestionLayout.count():
            item = ui.dsmLevelTwoManiaQuestionLayout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
        ui.dsmLevelTwoManiaNextButton.setVisible(False)

        # Add big submit button
        submit_btn = QPushButton("Submit")
        submit_btn.setMinimumHeight(50)
        submit_btn.setStyleSheet("background-color: green; color: white; font-size: 18px;")
        submit_btn.clicked.connect(submit)
        ui.dsmLevelTwoManiaQuestionLayout.addWidget(submit_btn)
        print("[DEBUG] Submit button added!")

    def submit():
        total_raw = sum(selected_scores.values())
        print(f"[RESULT] Raw Total: {total_raw}")

        severity = "Low Risk"
        if total_raw >= 6:
            severity = "Possible Mania/Hypomania — follow-up needed."
            sendNotification("Possible Mania/Hypomania — follow-up needed.")
            sendLog("Possible Mania flagged")

        print(f"[RESULT] Raw: {total_raw} => Severity: {severity}")

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        result_key = f"dsm_level_two_mania_{timestamp}"

        results = {
            "questions": {
                f"Q{q + 1}": selected_answers[q] for q in selected_answers
            },
            "total_raw_score": total_raw,
            "severity": severity
        }

        results_dir = f"TomoBrain/Data/Users/{username}/Results"
        os.makedirs(results_dir, exist_ok=True)
        results_file = os.path.join(results_dir, "dsm_level_two_mania_results.json")

        all_results = {}
        if os.path.exists(results_file):
            with open(results_file, "r") as f:
                try:
                    all_results = json.load(f)
                except Exception:
                    all_results = {}

        all_results[result_key] = results

        with open(results_file, "w") as f:
            json.dump(all_results, f, indent=4)

        print(f"[INFO] Saved results to: {results_file}")
        ui.stackedWidget.setCurrentWidget(ui.Dashboard)

    ui.dsmLevelTwoManiaNextButton.setEnabled(False)
    ui.dsmLevelTwoManiaNextButton.setText("Next")
    ui.dsmLevelTwoManiaNextButton.clicked.connect(go_next)

    show_question(current_idx)





def run_dsm_level_two_irritability(ui):
    """
    Runs DSM Level Two Irritability Test for children only.
    Saves results under Results folder per user.
    """

    import os
    import json
    from datetime import datetime
    import pandas as pd
    from PySide6.QtWidgets import QPushButton

    selected_scores = {}
    selected_answers = {}
    current_idx = 0
    answer_buttons = []

    # ✅ Load current user info
    with open("TomoBrain/Data/Users/current_user.json") as f:
        user_data = json.load(f)
    username = user_data.get("username", "unknown")

    ui.dsmLevelTwoIrritabilityTitleLabel.setText("DSM Level Two Irritability")

    print(f"[DEBUG] Running DSM Level Two Irritability — Child Only")

    # ✅ Load questions (no header!)
    df = pd.read_excel(
        "TomoBrain/Data/Tests/dsm_level_two_irritability.xlsx",
        sheet_name="Child",
        header=None
    )
    questions = df[0].dropna().tolist()
    print(f"[DEBUG] Loaded {len(questions)} questions")

    def show_question(idx):
        nonlocal answer_buttons
        ui.dsmLevelTwoIrritabilityNextButton.setEnabled(False)
        ui.dsmLevelTwoIrritabilityNextButton.setVisible(True)
        answer_buttons = []

        if idx >= len(questions):
            show_submit()
            return

        question = questions[idx]
        ui.dsmLevelTwoIrritabilityLabel.setText(question)

        print(f"[DEBUG] Q{idx + 1}: {question}")

        while ui.dsmLevelTwoIrritabilityQuestionLayout.count():
            item = ui.dsmLevelTwoIrritabilityQuestionLayout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        labels = [
            ("Not True", 0),
            ("Somewhat True", 1),
            ("Certainly True", 2)
        ]

        for text, score in labels:
            btn = QPushButton(text)
            btn.setStyleSheet("background-color: white; color: black; font-size:24px;")
            btn.clicked.connect(lambda _, s=score, t=text, b=btn: handle_answer(s, t, b, idx))
            ui.dsmLevelTwoIrritabilityQuestionLayout.addWidget(btn)
            answer_buttons.append(btn)

    def handle_answer(score, answer_text, clicked_button, q_idx):
        selected_scores[q_idx] = score
        selected_answers[q_idx] = {"answer_text": answer_text, "score": score}

        for btn in answer_buttons:
            btn.setStyleSheet("background-color: white; color: black;")
        clicked_button.setStyleSheet("background-color: #008060; color: white;")

        print(f"[DEBUG] Q{q_idx + 1} | {answer_text} ({score})")
        ui.dsmLevelTwoIrritabilityNextButton.setEnabled(True)

    def go_next():
        nonlocal current_idx
        current_idx += 1
        show_question(current_idx)

    def show_submit():
        # --- Clear the layout and hide Next, add big Submit button like DSM Level One ---
        ui.dsmLevelTwoIrritabilityLabel.setText("All done! Click Submit to save your results.")
        while ui.dsmLevelTwoIrritabilityQuestionLayout.count():
            item = ui.dsmLevelTwoIrritabilityQuestionLayout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
        ui.dsmLevelTwoIrritabilityNextButton.setVisible(False)

        submit_btn = QPushButton("Submit")
        submit_btn.setMinimumHeight(50)
        submit_btn.setStyleSheet("background-color: green; color: white; font-size: 18px;")
        submit_btn.clicked.connect(submit)
        ui.dsmLevelTwoIrritabilityQuestionLayout.addWidget(submit_btn)
        print("[DEBUG] Submit button added!")

    def submit():
        answered_first_six = [selected_scores.get(i) for i in range(6)]
        answered_count = sum(1 for s in answered_first_six if s is not None)

        if answered_count < 4:
            print("[WARN] More than 2 of first 6 are missing — cannot score.")
            return

        raw_first_six = sum(s for s in answered_first_six if s is not None)

        if answered_count < 6:
            # Prorate
            prorated_raw = raw_first_six * 6 / answered_count
            total_raw = round(prorated_raw, 2)
            print(f"[INFO] Prorated Raw: {total_raw} (Answered: {answered_count})")
        else:
            total_raw = raw_first_six

        avg_score = round(total_raw / 6, 2)

        # Map severity
        if avg_score == 0:
            severity = "None"
        elif avg_score == 1:
            severity = "Mild-Moderate"
        elif avg_score == 2:
            severity = "Moderate-Severe"
        else:
            severity = "Mixed/Check Scores"

        print(f"[RESULT] Raw: {total_raw} => Average: {avg_score} => Severity: {severity}")

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        result_key = f"dsm_level_two_irritability_{timestamp}"

        results = {
            "questions": {
                f"Q{q + 1}": selected_answers.get(q, {"answer_text": "Not Answered", "score": None})
                for q in range(len(questions))
            },
            "total_raw_score": total_raw,
            "average_score": avg_score,
            "severity": severity
        }

        results_dir = f"TomoBrain/Data/Users/{username}/Results"
        os.makedirs(results_dir, exist_ok=True)
        results_file = os.path.join(results_dir, "dsm_level_two_irritability_results.json")

        all_results = {}
        if os.path.exists(results_file):
            with open(results_file, "r") as f:
                try:
                    all_results = json.load(f)
                except Exception:
                    all_results = {}

        all_results[result_key] = results

        with open(results_file, "w") as f:
            json.dump(all_results, f, indent=4)

        print(f"[INFO] Saved results to: {results_file}")
        ui.stackedWidget.setCurrentWidget(ui.Dashboard)

    ui.dsmLevelTwoIrritabilityNextButton.setEnabled(False)
    ui.dsmLevelTwoIrritabilityNextButton.setText("Next")
    ui.dsmLevelTwoIrritabilityNextButton.setVisible(True)
    ui.dsmLevelTwoIrritabilityNextButton.clicked.connect(go_next)

    show_question(current_idx)


