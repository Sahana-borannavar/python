import pandas as pd

# Initial data
data = {
    'ID': [1, 2, 3],
    'Expense_Name': ['Groceries', 'Electricity Bill', 'Internet'],
    'Amount': [1500, 1200, 800]
}

# Create DataFrame
df = pd.DataFrame(data)

# Create CSV and JSON files
df.to_csv('expenses.csv', index=False)
df.to_json('expenses.json', orient='records')

# Add new record to CSV
new_expense = pd.DataFrame([{'ID': 4, 'Expense_Name': 'Transport', 'Amount': 500}])
df_csv = pd.read_csv('expenses.csv')
df_csv = pd.concat([df_csv, new_expense], ignore_index=True)
df_csv.to_csv('expenses.csv', index=False)

# Add new record to JSON
new_expense_json = pd.DataFrame([{'ID': 4, 'Expense_Name': 'Transport', 'Amount': 500}])
df_json = pd.read_json('expenses.json')
df_json = pd.concat([df_json, new_expense_json], ignore_index=True)
df_json.to_json('expenses.json', orient='records')

# Delete a record in CSV
df_csv = pd.read_csv('expenses.csv')
df_csv = df_csv[df_csv['Expense_Name'] != 'Groceries']
df_csv.to_csv('expenses.csv', index=False)

# Delete a record in JSON
df_json = pd.read_json('expenses.json')
df_json = df_json[df_json['Expense_Name'] != 'Groceries']
df_json.to_json('expenses.json', orient='records')

# Optional: Display final CSV and JSON data
print("CSV Data:\n", df_csv)
print("\nJSON Data:\n", df_json)
