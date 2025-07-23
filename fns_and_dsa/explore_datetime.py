import datetime

def display_current_datetime():
    current_date = datetime.datetime.now()
    print(f"Current Date and Time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")
    return current_date

def calculate_future_date(current_date, number_of_days):
    future_date = current_date + datetime.timedelta(days=number_of_days)
    print(f"Future Date after {number_of_days} days: {future_date.strftime('%Y-%m-%d')}")
    return future_date

# Part 1: Show current date and time
current = display_current_datetime()

# Part 2: Ask user for days and calculate future date
number_of_days = int(input("Enter the number of days to add: "))
calculate_future_date(current, number_of_days)