from faker import Faker
import pandas as pd
import random

# Initialize Faker
fake = Faker()

# Load FleetCompany data
fleet_company = pd.read_csv('fleet_company.csv')

# Generate dummy data for Card table
def generate_card_data(fleet_company):
    data = []
    for index, row in fleet_company.iterrows():
        company_id = row['FleetCompany_id']
        num_cards = random.randint(1, 10)  # Each company can have between 1 and 10 cards
        for card_number in range(1, num_cards + 1):
            record = {
                'Card_id': f"{company_id}{str(card_number).zfill(4)}",  # Format Card_id as FleetCompany_id_0001, 0002, etc.
                'FleetCompany_id': company_id,
                'Expiry_date': fake.date_between(start_date='today', end_date='+5y').strftime('%Y-%m-%d'),
                'Balance_spent': round(fake.pydecimal(min_value=0, max_value=5000), 2),
                'card_number': f"{str(card_number).zfill(4)}"  # Sequential card number formatted as 0001, 0002, etc.
            }
            data.append(record)
    return data

data = generate_card_data(fleet_company)
df = pd.DataFrame(data)

# Save DataFrame to Excel file
csv_file = 'card_data.csv'
df.to_csv(csv_file, index=False)
print(f"Card data saved to {csv_file}")
