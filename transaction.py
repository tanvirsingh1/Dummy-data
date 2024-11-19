import pandas as pd
import random
from faker import Faker

# Initialize Faker
fake = Faker()


# Generate dummy data for Transactions table
def generate_transaction_data(cards, addresses):
    data = []
    transaction_id = 1

    address_ids = addresses['Address_id'].tolist()  # Get list of valid Address_ids

    for index, row in cards.iterrows():
        card_id = row['Card_id']
        num_transactions_per_card = random.randint(1, 10)  # Random number of transactions between 1 and 10
        for _ in range(num_transactions_per_card):
            # Generate initial transaction details with zero values
            address_id = random.choice(address_ids)  # Choose a random Address_id
            time_date = fake.date_time_between(start_date='-1y', end_date='now') # 1 year worth of Transactions

            record = {
                'Transaction_id': str(transaction_id).zfill(6),  # Format Transaction_id with leading zeros
                'Card_id': card_id,
                'Subtotal': 0.00,  # Initialize Subtotal to 0
                'Tax': 0.00,       # Initialize Tax to 0
                'Total': 0.00,     # Initialize Total to 0
                'Address_id': address_id,
                'Time': time_date.strftime('%H:%M:%S'),
                'Date': time_date.strftime('%Y-%m-%d'),
                'IsFraud': None

            }
            data.append(record)
            transaction_id += 1

    return data


def main():
    # Load Card and Address data
    cards = pd.read_csv('card_data.csv')
    addresses = pd.read_csv('address_data.csv')  # Ensure this file contains Address_id

    # Generate data for transactions
    transaction_data = generate_transaction_data(cards, addresses)
    df_transactions = pd.DataFrame(transaction_data)

    # Save DataFrame to CSV file (overwrite)
    csv_file_transactions = 'transaction_data.csv'
    df_transactions.to_csv(csv_file_transactions, index=False)

    print(f"Transaction data initialized and saved to {csv_file_transactions}")

if __name__ == "__main__":
    main()