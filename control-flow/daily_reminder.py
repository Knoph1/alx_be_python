# daily_reminder.py

# Prompt for a single task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize reminder message
reminder_message = ""

# Process the task based on priority using Match Case
match priority:
    case "high":
        reminder_message = f"'{task}' is a high priority task"
    case "medium":
        reminder_message = f"'{task}' is a medium priority task"
    case "low":
        reminder_message = f"'{task}' is a low priority task"
    case _:
        reminder_message = "Priority level not recognized. Please enter high, medium, or low."

# Modify reminder based on time sensitivity
if time_bound == "yes":
    reminder_message += " that requires immediate attention today!"
else:
    reminder_message += ". Consider completing it when you have free time."

# Print the customized reminder
print(reminder_message)

# Optionally, a message about celebrating the milestone
print("\nWell done on completing this project! Let the world hear about this milestone achieved.\n🚀 Click here to tweet! 🚀")
