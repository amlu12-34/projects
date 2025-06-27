from datetime import datetime

def calculate_age():
    birth_date_input = input("Enter your date of birth (YYYY-MM-DD): ")
    try:
        birth_date = datetime.strptime(birth_date_input, "%Y-%m-%d")
        today = datetime.today()

        age = today.year - birth_date.year

        # Check if birthday has occurred this year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1

        print(f"You are {age} years old.")

    except ValueError:
        print("Invalid date format. Please enter the date in YYYY-MM-DD format.")

calculate_age()
