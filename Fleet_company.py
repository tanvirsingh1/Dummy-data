from faker import Faker
import pandas as pd
import random
# Initialize Faker
fake = Faker()

# Generate dummy data
address_df = pd.read_csv('address_data.csv')

def generate_fuelCompany(num_records,address_ids):
    data = []
    for _ in range(num_records):
        address_id = random.choice(address_ids)
        fleet_company_id = '997' + str(random.randint(1000000, 9999999))
        record = {
      'FleetCompany_id': fleet_company_id,
      'Company_id' : 115,
      'FleetCompany_Name': fake.company(),
      'FleetCompany_Email': fake.email(),
      'Address_id' :address_id,
      'FleetCompany_Phone': fake.phone_number(),
      'FleetCompany_Credit_Limit': round(fake.random_number(digits=6, fix_len=True) + random.random(), 2)

        }
        data.append(record)
    return data

# Create DataFrame and save to csv
num_records = 10
address_ids = address_df['Address_id'].tolist()
data = generate_fuelCompany(num_records, address_ids)
df = pd.DataFrame(data)
# Save DataFrame to Excel file
csv_file = 'fleet_company.csv'
df.to_csv(csv_file, index=False)

print(f"Data saved to {csv_file}")
# Once this is generated Create the data for Cards linked

