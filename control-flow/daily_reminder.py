# daily_reminder.py
# A simple reminder script based on priority and time sensitivity

# Prompt for a Single Task
task = input("Enter your task for today: ")
priority = input("Set the priority level (high, medium, low): ").lower()
time_bound = input("Is the task time-bound? (yes or no): ").lower()

# Process the Task Based on Priority
match priority:
    case "high":
        reminder = f"🔴 HIGH PRIORITY: {task}"
    case "medium":
        reminder = f"🟡 MEDIUM PRIORITY: {task}"
    case "low":
        reminder = f"🟢 LOW PRIORITY: {task}"
    case _:
        reminder = f"⚪ UNKNOWN PRIORITY: {task}"

# Adjust message based on time sensitivity
if time_bound == "yes":
    reminder += " — that requires immediate attention today!"

# Print the customized reminder
print("\n📌 Reminder:")
print(reminder)