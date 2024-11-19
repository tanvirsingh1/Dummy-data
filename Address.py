import random
from faker import Faker
import pandas as pd

# Initialize Faker
fake = Faker("en_CA")  # Set locale to Canada


# Generate dummy data for Address table
def generate_address_data(num_records):
    data = []
    unique_ids = set()

    # Generate unique IDs
    while len(unique_ids) < num_records:
        unique_ids.add(random.randint(1, 10000))  # Use Python's random for unique IDs

    for unique_id in unique_ids:
        record = {
            'Address_id': unique_id,
            'City': fake.city(),
            'Province': fake.province(),  # Corrected to generate Canadian provinces
            'Postal_Code': fake.postalcode(),  # Canadian postal codes
            'Country': "Canada",
            'Street': fake.street_address()
        }
        data.append(record)
    return data


def main():
    num_records = 100
    data = generate_address_data(num_records)

    # Create a DataFrame and save to CSV
    df = pd.DataFrame(data)
    csv_file = 'address_data.csv'
    df.to_csv(csv_file, index=False)

    print(f"Address data saved to {csv_file}")

if __name__ == "__main__":
    main()