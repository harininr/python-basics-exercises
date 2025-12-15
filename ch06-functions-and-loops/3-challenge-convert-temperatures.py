# 6.3 - Challenge: Convert temperatures
# Solution to challenge


def get_numeric_input(prompt):
    """Prompt the user until a valid numeric input is entered."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def convert_cel_to_far(temp_cel):
    """Return the Celsius temperature temp_cel converted to Fahrenheit."""
    return temp_cel * (9 / 5) + 32


def convert_far_to_cel(temp_far):
    """Return the Fahrenheit temperature temp_far converted to Celsius."""
    return (temp_far - 32) * (5 / 9)



# Prompt the user to input a Fahrenheit temperature.
temp_far = get_numeric_input("Enter a temperature in degrees F: ")

# Convert the temperature to Celsius.
temp_cel = convert_far_to_cel(temp_far)

# Display the converted temperature
print(f"{temp_far} degrees F = {temp_cel:.2f} degrees C")

# Prompt the user to input a Celsius temperature.
temp_cel = get_numeric_input("\nEnter a temperature in degrees C: ")

# Convert the temperature to Fahrenheit.
temp_far = convert_cel_to_far(temp_cel)

# Display the converted temperature
print(f"{temp_cel} degrees C = {temp_far:.2f} degrees F")
