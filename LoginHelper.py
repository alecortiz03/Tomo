import bcrypt
import os
import json

def checkLogin():
    users_file = "TomoBrain/Data/Users/current_user.json"
    return os.path.exists(users_file)

def registerSubmit(ui):
    firstName = ui.firstNameInput.text()
    lastName = ui.lastNameInput.text()
    username = ui.usernameInput.text()
    password = ui.passwordInput.text()
    age = ui.ageInput.text()
    gender = ui.genderComboBox.currentText()
    print(f"First Name: {firstName}")
    print(f"Last Name: {lastName}")
    print("Username:", username)
    print("Password:", password)
    print(f"Age: {age}")
    print(f"Gender: {gender}")
    if not all([firstName, lastName, username, password, age, gender]):
        return "All Fields Not Filled"
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
    users_file = "TomoBrain/Data/Users/users.json"
    if os.path.exists(users_file):
        with open(users_file, "r") as f:
            users = json.load(f)
    else:
        users = {}

    if username in users:
        return "Username Already Made"

    users[username] = {
        "first_name": firstName,
        "last_name": lastName,
        "password": hashed_password,
        "age": age,
        "gender": gender
        }
    os.makedirs("TomoBrain/Data/Users", exist_ok=True)
    with open(users_file, "w") as f:
        json.dump(users, f, indent=2)

    user_dir = f"TomoBrain/Data/Users/{username}"
    os.makedirs(user_dir, exist_ok=True)

    chat_history_path = os.path.join(user_dir, "chat_history.json")
    if not os.path.exists(chat_history_path):
        with open(chat_history_path, "w") as f:
            json.dump([
                {"role": "system", "content": f"You are a licensed therapy bot who helps users manage stress and emotional discomfort. You provide simple and effective ways to relax, cope, or feel better. If a user asks a question unrelated to stress, mental health, or self-care, politely decline and explain that your role is limited to emotional support. All your answers must be concise, no more than 2 to 3 short sentences. Address the user as {firstName}."},
                {"role": "user", "content": "What is my name?"},
                {"role": "assistant", "content": f"Your name is {firstName}!"}
                ], f, indent=2)
    notificationPath = f"TomoBrain/Data/Users/{username}/notifications.json"
    notifications = ["Take DSM Level One"]
    with open(notificationPath, "w") as f:
        json.dump(notifications,f, indent=4)

    return "Complete"
def loginSubmit(ui):
    username = ui.usernameLoginInput.text()
    password = ui.passwordLoginInput.text()

    if not username or not password:
        return "All Fields Not Filled"

    users_file = "TomoBrain/Data/Users/users.json"
    if not os.path.exists(users_file):
        return "No Users"

    with open(users_file, "r") as f:
        users = json.load(f)

    user = users.get(username)
    if not user:
        return "Failed Login"

    if bcrypt.checkpw(password.encode("utf-8"), user["password"].encode("utf-8")):
        sessionData = {
            "first_name": user["first_name"],
            "last_name": user["last_name"],
            "username": username ,
            "password": user["password"] ,
            "age": user["age"],
            "gender": user["gender"]
            }
    else:
        return "Failed Login"
    with open("TomoBrain/Data/Users/current_user.json", "w") as f:
        json.dump(sessionData, f, indent=2)
        return "Complete"
def logout():
    os.remove("TomoBrain/Data/Users/current_user.json")

