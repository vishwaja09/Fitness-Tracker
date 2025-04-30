import json

# Load the JSON data from the file
with open("exercise_log.json", "r") as file:
    data = json.load(file)

# Initialize total calories
total_calories = 0

# Print each exercise and add up calories
print("Exercise Log:")
for entry in data:
    print(f"- Type: {entry['type']}, Duration: {entry['duration']} mins, Calories: {entry['calories']}")
    total_calories += entry["calories"]

print(f"\nTotal Calories Burned: {total_calories} kcal")
