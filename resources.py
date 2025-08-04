from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget, QLabel, QPushButton

def load_resources(ui):
    # Transparent background for scroll area and contents
    scroll_widget = ui.resourcesScrollArea
    scroll_widget.setStyleSheet("background: transparent;")
    ui.resultsScrollArea.setStyleSheet("background: transparent; border: none;")

    # Ensure a QVBoxLayout exists on the scroll widget
    if scroll_widget.layout() is None:
        layout = QVBoxLayout(scroll_widget)
    else:
        layout = scroll_widget.layout()

    # Remove any existing widgets
    while layout.count():
        item = layout.takeAt(0)
        if item.widget():
            item.widget().deleteLater()

    # --- Add Grounding resource row ---
    color_grounding = "#8ecae6"
    row_widget1 = QWidget()
    row_layout1 = QHBoxLayout(row_widget1)
    row_layout1.setContentsMargins(22, 8, 22, 8)
    row_layout1.setSpacing(16)

    row_widget1.setStyleSheet("""
        QWidget {
            border: 1.4px solid rgba(60,60,60,0.44);
            border-radius: 22px;
            background: rgba(32, 40, 54, 0.40);
            margin-bottom: 13px;
            backdrop-filter: blur(8px);
        }
    """)

    label1 = QLabel("Grounding")
    label1.setStyleSheet(f"""
        QLabel {{
            font-size: 20px;
            color: {color_grounding};
            font-weight: bold;
            background: transparent;
            border: none;
        }}
    """)
    label1.setWordWrap(True)

    button1 = QPushButton("Try Session")
    button1.setObjectName("tryGroundingSessionButton")
    ui.tryGroundingSessionButton = button1
    button1.setStyleSheet(f"""
        QPushButton {{
            background-color: {color_grounding};
            color: #232629;
            font-weight: bold;
            border-radius: 12px;
            padding: 7px 28px;
            margin-left: 20px;
        }}
        QPushButton:hover {{
            background-color: #219ebc;
        }}
    """)

    row_layout1.addWidget(label1)
    row_layout1.addStretch()
    row_layout1.addWidget(button1)
    layout.addWidget(row_widget1)

    # --- Add Box Breathing resource row ---
    color_box = "#90be6d"  # Use any color you like
    row_widget2 = QWidget()
    row_layout2 = QHBoxLayout(row_widget2)
    row_layout2.setContentsMargins(22, 8, 22, 8)
    row_layout2.setSpacing(16)

    row_widget2.setStyleSheet("""
        QWidget {
            border: 1.4px solid rgba(60,60,60,0.44);
            border-radius: 22px;
            background: rgba(32, 40, 54, 0.40);
            margin-bottom: 13px;
            backdrop-filter: blur(8px);
        }
    """)

    label2 = QLabel("Box Breathing Technique")
    label2.setStyleSheet(f"""
        QLabel {{
            font-size: 20px;
            color: {color_box};
            font-weight: bold;
            background: transparent;
            border: none;
        }}
    """)
    label2.setWordWrap(True)

    button2 = QPushButton("Try Session")
    button2.setObjectName("tryBoxBreathingButton")
    ui.tryBoxBreathingButton = button2
    button2.setStyleSheet(f"""
        QPushButton {{
            background-color: {color_box};
            color: #232629;
            font-weight: bold;
            border-radius: 12px;
            padding: 7px 28px;
            margin-left: 20px;
        }}
        QPushButton:hover {{
            background-color: #618b4a;
        }}
    """)

    row_layout2.addWidget(label2)
    row_layout2.addStretch()
    row_layout2.addWidget(button2)
    layout.addWidget(row_widget2)

    layout.addStretch()




