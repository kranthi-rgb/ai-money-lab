def get_message(mood):
    if mood == "happy":
        return "Keep smiling. Your energy changes the world."
    elif mood == "sad":
        return "Every champion fights silent battles. Keep going."
    elif mood == "tired":
        return "Rest if needed, but never quit your mission."
    elif mood == "motivated":
        return "Focus sharp. Discipline wins everything."
    else:
        return "No matter your mood, move forward today."


def save_log(mood, message):
    with open("daily_mood_log.txt", "a") as file:
        file.write("Mood: " + mood + "\n")
        file.write("Message: " + message + "\n")
        file.write("----------------------\n")


mood = input("How are you feeling today? ").strip().lower()
message = get_message(mood)

print("\nAI Message:")
print(message)

save_log(mood, message)