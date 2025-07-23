# temp_conversion_tool.py

FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    temp_input = input("Enter the temperature (e.g., 98.6): ")
    unit = input("Is this in Celsius or Fahrenheit? (C/F): ").upper()

    if not temp_input.replace('.', '', 1).lstrip('-').isdigit():
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    temperature = float(temp_input)

    if unit == 'F':
        result = convert_to_celsius(temperature)
        print(f"{temperature}°F is {result:.2f}°C")
    elif unit == 'C':
        result = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {result:.2f}°F")
    else:
        raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()