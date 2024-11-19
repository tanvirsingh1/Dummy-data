import pandas as pd
import random

# Define price ranges for fuel products
fuel_products = {
    'Gasoline': 8.00,  # Fixed price per litre
    'Diesel': 4.50,  # Fixed price per litre
    'Motor Oil': 11.00,  # Fixed price per litre
    'Antifreeze': 15.00,  # Fixed price per litre
    'Fuel Injector Cleaner': 10.00,  # Fixed price per litre
    'Fuel Stabilizer': 8.50,  # Fixed price per litre
    'G-fuel': 2.99,
    'Gas Premium': 14.00,
    'Dyed Diesel': 22.00
}

# Define fixed prices for non-fuel products
non_fuel_products = {
    'Cigarettes': 10.00,  # Fixed price per pack
    'Lottery Ticket': 2.00,  # Fixed price per ticket
    'Grocery Item': 5.00,  # Fixed price per item
    'Car Wash': 5.00
}


# Function to get product price and type
def get_product_details(product_name):
    if product_name in fuel_products:
        # Return price and type for fuel products
        return fuel_products[product_name], 'Fuel'
    elif product_name in non_fuel_products:
        # Return price and type for non-fuel products
        return non_fuel_products[product_name], 'Non-Fuel'
    else:
        raise ValueError(f"Unknown product: {product_name}")


# Generate data for a mixed list of products
def generate_product_data():
    # Combine fuel and non-fuel products into one list
    all_products = list(fuel_products.keys()) + list(non_fuel_products.keys())

    # Shuffle the combined list to mix fuel and non-fuel products
    random.shuffle(all_products)

    data = []
    for product_id, product_name in enumerate(all_products, start=1):
        product_price, product_type = get_product_details(product_name)
        record = {
            'Product_id': str(product_id).zfill(4),  # Format Product_id with leading zeros
            'Product_name': product_name,  # Use the chosen product name
            'Product_price': product_price,  # Add product price
            'Product_type': product_type  # Add product type (Fuel or Non-Fuel)
        }
        data.append(record)

    return data

def main():
    # Generate product data
    data = generate_product_data()
    df = pd.DataFrame(data)

    # Save DataFrame to CSV file
    csv_file = 'product_data.csv'
    df.to_csv(csv_file, index=False)

    print(f"Product data saved to {csv_file}")

if __name__ == "__main__":
    main()