# Project 3: Basic Voice Assistant
import datetime

def voice_assistant(command):
    cmd = command.lower()
    
    if "hello" in cmd or "hi" in cmd:
        return "Hello! I am your Virtual Assistant. How can I help?"
    elif "time" in cmd:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        return f"Current time is {current_time}"
    elif "date" in cmd:
        current_date = datetime.datetime.now().strftime("%d-%m-%Y")
        return f"Today's date is {current_date}"
    elif "name" in cmd:
        return "I am OASIS Assistant, created by Dhanashri Gawali"
    elif "oasis" in cmd:
        return "OASIS Infobyte provides great internships!"
    else:
        return "I can tell time, date, and greet you. Try 'hello', 'time', 'date'"

# --- DEMO ---
# Input() use nahi kela mhanun Jupyter error yenar nahi

print("Testing Voice Assistant:\n")

# Test 1
user_command = "hello"
print(f"You: {user_command}")
print(f"Assistant: {voice_assistant(user_command)}\n")

# Test 2
user_command = "what is the time"
print(f"You: {user_command}")
print(f"Assistant: {voice_assistant(user_command)}\n")

# Test 3
user_command = "your name"
print(f"You: {user_command}")
print(f"Assistant: {voice_assistant(user_command)}")