import pandas as pd
import random



# Generate dummy data for Purchase Line table
def generate_purchase_line_data(transaction_ids, lines_per_transaction,products):
    data = []
    purchase_line_id = 1  # Start with Purchase_Line_id 1

    for transaction_id in transaction_ids:
        for _ in range(lines_per_transaction):
            # Randomly choose a product
            product = products.sample(1).iloc[0]  # Select a random product
            price = product['Product_price']

            # Determine a random quantity
            quantity = random.randint(1, 100)  # Random quantity between 1 and 3
            total_price = round(quantity * price, 2)  # Calculate total price for this line

            record = {
                'Purchase_Line_id': str(purchase_line_id).zfill(6),  # Format Purchase_Line_id with leading zeros
                'Transaction_id': transaction_id,
                'Product_name': product['Product_name'],
                'Quantity': quantity,
                'Total_price': total_price
            }
            data.append(record)
            purchase_line_id += 1  # Increment Purchase_Line_id for the next record

    return data


def main():
    # Load Product data
    products = pd.read_csv('product_data.csv')
    # Load transaction data to get Transaction IDs
    transactions = pd.read_csv('transaction_data.csv')
    transaction_ids = transactions['Transaction_id'].tolist()

    # Defines how many purchase lines you want to create per transaction
    lines_per_transaction = 4  # For example, 3 purchase lines per transaction

    # Generate purchase line data
    purchase_lines_data = generate_purchase_line_data(transaction_ids, lines_per_transaction,products)
    df_purchase_lines = pd.DataFrame(purchase_lines_data)

    # Save DataFrame to CSV file
    csv_file_purchase_lines = 'purchase_line_data.csv'
    df_purchase_lines.to_csv(csv_file_purchase_lines, index=False)

    print(f"Purchase line data saved to {csv_file_purchase_lines}")

if __name__ == "__main__":
    main()