from datetime import date

today = date.today()
name = input("Enter your name: ")
goal = input("Enter your goal: ")

message = f"""
Date: {today},

Hello {name},
Your mission is clear: {goal}.
Execute daily. No excuses.
"""


print(message)

with open("daily_motivation.txt", "w") as file:
    file.write(message)

print("Saved to daily_motivation.txt")