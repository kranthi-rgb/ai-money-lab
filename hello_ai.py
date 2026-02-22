from datetime import date
from pathlib import Path


def get_user_input():
    """Collect and validate user input."""
    name = input("Enter your name: ").strip()
    goal = input("Enter your goal: ").strip()

    if not name or not goal:
        raise ValueError("Name and goal cannot be empty.")

    return name, goal


def create_message(name: str, goal: str) -> str:
    """Generate motivational message."""
    today = date.today()

    message = (
        f"\nDate: {today}\n\n"
        f"Hello {name},\n"
        f"Your mission is clear: {goal}.\n"
        f"Execute daily. No excuses.\n"
    )

    return message


def save_message(message: str, filename: str = "daily_motivation.txt"):
    """Save message safely to file."""
    file_path = Path(filename)

    try:
        file_path.write_text(message, encoding="utf-8")
        print(f"✅ Message saved to {file_path.resolve()}")
    except Exception as e:
        print(f"❌ Failed to save file: {e}")


def main():
    """Program entry point."""
    print("\n🧠 AI Motivation Generator\n")

    try:
        name, goal = get_user_input()
        message = create_message(name, goal)

        print(message)
        save_message(message)

    except ValueError as error:
        print(f"⚠️ Input Error: {error}")


if __name__ == "__main__":
    main()