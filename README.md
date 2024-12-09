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
