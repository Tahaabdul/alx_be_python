# Ask for the task description
task = input("Enter your task: ")

# Ask for the priority level
priority = input("Priority (high/medium/low): ")

# Ask if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ")

# Create a basic reminder message
if priority == "high":
    reminder = f"Your task '{task}' is high priority."
elif priority == "medium":
    reminder = f"Your task '{task}' is medium priority."
elif priority == "low":
    reminder = f"Your task '{task}' is low priority."
else:
    reminder = "Invalid priority level."

# Add urgency if the task is time-sensitive
if time_bound == "yes":
    reminder += " This requires immediate attention!"

print(reminder) # Print the reminder