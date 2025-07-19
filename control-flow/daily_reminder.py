# daily_reminder.py

# Prompt for a Single Task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Process the Task Based on Priority using Match Case
match priority:
    case "high":
        reminder = f"HIGH PRIORITY: {task}"
    case "medium":
        reminder = f"MEDIUM PRIORITY: {task}"
    case "low":
        reminder = f"LOW PRIORITY: {task}"
    case _:
        reminder = f"UNKNOWN PRIORITY: {task}"

# Modify the reminder if time-bound
if time_bound == "yes":
    reminder += " — that requires immediate attention today!"

# Provide a Customized Reminder
print("Reminder:")
print(reminder)