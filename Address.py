from faker import Faker
import pandas as pd

# Initialize Faker
fake = Faker()

# Generate dummy data for Address table
def generate_address_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            'Address_id': fake.unique.random_int(min=1, max=10000),
            'Street': fake.street_address(),
            'City': fake.city(),
            'Province': fake.state(),
            'Postal_Code': fake.postcode(),
            'Country': fake.country()
        }
        data.append(record)
    return data

# Create DataFrame and save to  csv
num_records = 2
data = generate_address_data(num_records)
df = pd.DataFrame(data)


csv_file = 'address_data.csv'
df.to_csv(csv_file, index=False)

print(f"Address data saved to {csv_file}")