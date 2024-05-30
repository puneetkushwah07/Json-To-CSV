import pandas as pd

# Load the JSON data
json_file_path = 'shopify-data.json'
data = pd.read_json(json_file_path)

# Convert JSON data to CSV
csv_file_path = 'shopify-data.csv'
data.to_csv(csv_file_path, index=False)

print(f"JSON data has been converted to CSV successfully and saved as {csv_file_path}.")