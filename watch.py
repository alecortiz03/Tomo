import os
import json
import re

def store_paired_watch_mac_from_ui(ui):
    # Grab and sanitize MAC address from the line edit
    mac_address = ui.pairLineEdit.text().strip().upper()

    # Validate MAC format (AA:BB:CC:DD:EE:FF)
    if not re.match(r'^([0-9A-F]{2}:){5}[0-9A-F]{2}$', mac_address):
        print(f"[ERROR] Invalid MAC address format: {mac_address}")
        return

    # Load current user
    current_user_path = "TomoBrain/Data/Users/current_user.json"
    with open(current_user_path, "r") as f:
        user_info = json.load(f)
    username = user_info["username"]

    # File to store paired watches
    paired_file = os.path.join("TomoBrain", "Data", "pairedWatches.json")
    os.makedirs(os.path.dirname(paired_file), exist_ok=True)

    # Load existing dictionary or create new
    if os.path.exists(paired_file):
        with open(paired_file, "r") as f:
            try:
                paired_dict = json.load(f)
            except Exception:
                paired_dict = {}
    else:
        paired_dict = {}

    # Add if not already present
    if mac_address not in paired_dict:
        paired_dict[mac_address] = username
        with open(paired_file, "w") as f:
            json.dump(paired_dict, f, indent=2)
        print(f"[INFO] MAC address {mac_address} paired to {username} in {paired_file}")
    else:
        print(f"[INFO] MAC address {mac_address} already paired.")

