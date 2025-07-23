from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current Date and Time: {formatted_date}")
    return formatted_date  # Required to return formatted date

def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date: "))  # Exact prompt required
    current_date = datetime.now()
    future_date = current_date + timedelta(days=number_of_days)
    formatted_future = future_date.strftime("%Y-%m-%d")
    print(f"Future Date: {formatted_future}")
    return formatted_future

# Call both functions
display_current_datetime()
calculate_future_date()