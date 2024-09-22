# Ask for the task description
task = input("Enter your task: ")

# Ask for the priority level
priority = input("Priority (high/medium/low): ")

# Ask if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ")

# Create a reminder message based on priority using match case
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = "Invalid priority level."

# Check if the task is time-sensitive
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
elif priority in ["high", "medium", "low"]:
    reminder += ". Consider completing it when you have free time."

# Print the customized reminder
print("Reminder:", reminder)
