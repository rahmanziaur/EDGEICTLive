# EDGEICT

import pandas as pd

# Load the CSV file
csv_file = 'your_file.csv'  # Replace with the path to your CSV file
data = pd.read_csv(csv_file)

# Ensure the 'Email' column exists
if 'Email' in data.columns:
    # Extract email addresses and join them with commas
    email_addresses = ', '.join(data['Email'].dropna().astype(str).tolist())
    print(email_addresses)
else:
    print("The 'Email' column does not exist in the CSV file.")

### Calculate PI up to given digits and sum all the digits after decimal.

from mpmath import mp

def calculate_pi_and_sum_digits(decimal_places):
    # Set the precision for pi calculation
    mp.dps = decimal_places + 2  # Extra precision to avoid rounding issues
    pi_value = str(mp.pi)
    
    # Get the digits after the decimal point
    digits_after_decimal = pi_value.split('.')[1][:decimal_places]
    
    # Sum all the digits after the decimal point
    digit_sum = sum(int(digit) for digit in digits_after_decimal)
    
    return pi_value[:decimal_places + 2], digit_sum


# Input the number of decimal places
decimal_places = int(input("Enter the number of decimal places for π: "))

# Calculate and display the result
pi_value, digit_sum = calculate_pi_and_sum_digits(decimal_places)
print(f"π to {decimal_places} decimal places: {pi_value}")
print(f"Sum of digits after the decimal point: {digit_sum}")
