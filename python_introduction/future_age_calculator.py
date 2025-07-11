# future_age_calculator.py

# Prompt user for their current age
current_age = int(input("How old are you? "))

# Define the current year and target year
current_year = 2023
target_year = 2050
years_to_add = target_year - current_year

# Calculate future age
future_age = current_age + years_to_add

# Output result
print("In 2050, you will be", future_age, "years old.")

