import random
from datetime import datetime
import json

# 1. Dictionary of moods with multiple messages
mood_messages = {
    "happy": [
        "Keep smiling. Your energy changes the world.",
        "Happiness is contagious. Spread it!",
        "Your joy can light up someone's day."
    ],
    "sad": [
        "Every champion fights silent battles. Keep going.",
        "It's okay to feel sad. This will pass.",
        "Storms make trees take deeper roots. Stay strong."
    ],
    "tired": [
        "Rest if needed, but never quit your mission.",
        "Take a deep breath. Your body needs it.",
        "Recharge yourself. Then conquer the day."
    ],
    "motivated": [
        "Focus sharp. Discipline wins everything.",
        "Push beyond limits. Success awaits.",
        "Your energy today builds your future."
    ]
}

def get_message(mood):
    """Return a random message for the given mood."""
    if mood in mood_messages:
        return random.choice(mood_messages[mood])
    else:
        return "No matter your mood, move forward today."

def save_log(mood, message):
    """Save mood, message, and timestamp to a JSON log."""
    log_entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "mood": mood,
        "message": message
    }
    try:
        # Read existing logs
        with open("daily_mood_log.json", "r") as file:
            logs = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        logs = []

    logs.append(log_entry)
    
    # Save updated logs
    with open("daily_mood_log.json", "w") as file:
        json.dump(logs, file, indent=4)

def main():
    print("Hello! I'm your daily mood AI assistant.")
    mood = input("How are you feeling today? ").strip().lower()
    message = get_message(mood)
    
    print("\n🌟 AI Message:")
    print(message)
    
    save_log(mood, message)
    
    # Optional follow-up for certain moods
    if mood == "sad":
        print("\n💡 Tip: Try writing down one thing you're grateful for today.")
    elif mood == "tired":
        print("\n💡 Tip: Take a 10-minute power nap or stretch to refresh yourself.")

if __name__ == "__main__":
    main()