from datetime import date

def calculate_age(birth_year, birth_month, birth_day, current_date):
    # Adjust age calculation based on whether the birthday has passed
    age = current_date.year - birth_year - ((current_date.month, current_date.day) < (birth_month, birth_day))
    return age

# Birth date
birth_year = 1996
birth_month = 2
birth_day = 29

# Test date (set to February 28, 2024)
test_date = date(2024, 2, 28)

# Calculate and print the age
age = calculate_age(birth_year, birth_month, birth_day, test_date)
print(f"Your age is: {age}")

