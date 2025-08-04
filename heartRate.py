import os
import json
import matplotlib.pyplot as plt
from io import BytesIO
from PIL.ImageQt import ImageQt
from PIL import Image
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

def getHeartRate(ui):
    user_json_path = "TomoBrain/Data/Users/current_user.json"
    if not os.path.exists(user_json_path):
        print(f"[ERROR] No current user at {user_json_path}")
        return None
    with open(user_json_path, "r", encoding="utf-8") as f:
        user_data = json.load(f)
    username = user_data.get("username")
    if not username:
        print("[ERROR] Username not found in current_user.json")
        return None

    heartRateFolderPath = f"TomoBrain/Data/Users/{username}/HeartRateStats/heartRate.json"

    # Check if file exists
    if not os.path.exists(heartRateFolderPath):
        ui.heartRateGraph.setText("No Data Found Yet")
        ui.heartRateGraph.setStyleSheet("font-size:20px; color:black;")
    else:
        with open(heartRateFolderPath, 'r') as f:
            data = json.load(f)

        # Expect data is a list of ints
        if not isinstance(data, list) or not data:
            ui.heartRateGraph.setText("No Data Found Yet")
            ui.heartRateGraph.setStyleSheet("font-size:20px; color:black;")
            return

        values = data
        x_vals = list(range(1, len(values) + 1))

        # Set figure size to match label dimensions
        fig_width, fig_height, dpi = 6.71, 4.51, 100
        fig, ax = plt.subplots(figsize=(fig_width, fig_height), dpi=dpi)
        ax.plot(x_vals, values, marker='o', color='red')
        ax.set_xlabel("Sample")
        ax.set_ylabel("Heart Rate", fontweight='bold')
        ax.set_title("Heart Rate Over Time", fontweight='bold')
        ax.get_xaxis().set_visible(False)
        fig.autofmt_xdate()
        fig.patch.set_facecolor('black')
        ax.set_facecolor('black')
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')
        ax.xaxis.label.set_color('white')
        ax.yaxis.label.set_color('white')
        ax.title.set_color('white')
        for spine in ax.spines.values():
            spine.set_color('white')

        plt.tight_layout()

        # Save to buffer
        buf = BytesIO()
        plt.savefig(buf, format='png', dpi=dpi)
        plt.close(fig)
        buf.seek(0)

        # Load as QPixmap
        img = Image.open(buf)
        qt_img = ImageQt(img)
        pixmap = QPixmap.fromImage(qt_img)

        # --- Optionally, scale pixmap to fit label exactly ---
        pixmap = pixmap.scaled(671, 451, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        # Set to label
        ui.heartRateGraph.setPixmap(pixmap)
        ui.heartRateGraph.setAlignment(Qt.AlignCenter)
        print(data)
