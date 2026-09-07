import keyword

# Part 2 - Ask the three questions
person_name = input("Enter your name: ")
goal_name = input("Enter one skill you want to get better at: ")
target_month = input("Enter your target month: ")

# Part 3 - Store the practice time
daily_minutes = 30

# Part 4 - The heading
print("\nMY PERSONAL GOAL PLAN\n")

# Part 5 - The four plan lines
print("Name:", person_name)
print("Goal:", goal_name)
print("Target month:", target_month)
print("Daily practice:", daily_minutes, "minutes")

# Part 6 - Two lines that join up
print("Status:", end=" ")
print("Not started")

print("Reminder:", end=" - ")
print("Practise every day!")

# Part 7 - The sentence and the keywords
print("\nIn one sentence:")

print(
    person_name,
    "plans to work on",
    goal_name,
    "for",
    daily_minutes,
    "minutes every day until",
    target_month
)

print("\nWords Python has reserved for itself:\n")
print(keyword.kwlist)