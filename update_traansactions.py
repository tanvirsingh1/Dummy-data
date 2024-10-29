import pandas as pd

# Load transaction data
df_transactions = pd.read_csv('transaction_data.csv')

# Print the column names to debug
print(df_transactions.columns)

# Initialize columns if they do not exist
if 'Subtotal' not in df_transactions.columns:
    df_transactions['Subtotal'] = 0.0

if 'Tax' not in df_transactions.columns:
    df_transactions['Tax'] = 0.0

if 'Total' not in df_transactions.columns:
    df_transactions['Total'] = 0.0

# Load purchase line data
df_purchase_lines = pd.read_csv('purchase_line_data.csv')

# Calculate totals based on purchase lines
for index, row in df_transactions.iterrows():
    transaction_id = row['Transaction_id']

    # Filter purchase lines for this transaction
    purchase_lines = df_purchase_lines[df_purchase_lines['Transaction_id'] == transaction_id]

    # Calculate subtotal, tax (10%), and total
    subtotal = purchase_lines['Total_price'].sum()
    tax = subtotal * 0.13
    total = subtotal + tax

    # Update the transaction record
    df_transactions.at[index, 'Subtotal'] = subtotal
    df_transactions.at[index, 'Tax'] = tax
    df_transactions.at[index, 'Total'] = total

# Save the updated transaction data back to CSV
df_transactions.to_csv('transaction_data_updated.csv', index=False)

print("Transaction data updated and saved to 'transaction_data_updated.csv'")
