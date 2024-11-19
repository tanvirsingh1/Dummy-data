import pandas as pd

def main():
    df_transactions = pd.read_csv('transaction_data.csv')
    df_cards = pd.read_csv('card_data.csv')

    # Print the column names to debug
    print(df_transactions.columns)

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

    for index, row in df_cards.iterrows():
        card_id = row['Card_id']
        total_spent_per_card = df_transactions[df_transactions['Card_id'] == card_id]['Total'].sum()
        df_cards.at[index, 'Balance_spent'] = total_spent_per_card



    df_transactions.to_csv('transaction_data_updated.csv', index=False)
    df_cards.to_csv('cards_data_updated.csv', index=False)

    print("Transaction data and card balances updated and saved.")


if __name__ == "__main__":
    main()