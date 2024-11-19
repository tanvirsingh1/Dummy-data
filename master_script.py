# run_all.py

# Import all the scripts
import Address  # Will not run automatically anymore, since main is added
import Fleet_company  # Same as above
import cards  # Same as above
import transaction  # Same as above
import products  # Same as above
import PurchaseLine  # Same as above
import update_traansactions  # Same as above


def run_all():
    print("Running Address generation...")
    Address.main()
    print("Address generation finished.")

    print("Running Fleet Company generation...")
    Fleet_company.main()
    print("Fleet Company generation finished.")

    print("Running Cards generation...")
    cards.main()
    print("Cards generation finished.")

    print("Running Transactions generation...")
    transaction.main()
    print("Transactions generation finished.")

    print("Running Products generation...")
    products.main()
    print("Products generation finished.")

    print("Running Purchase Lines generation...")
    PurchaseLine.main()
    print("Purchase Lines generation finished.")

    print("Running Transactions update...")
    update_traansactions.main()
    print("Transactions update finished.")


if __name__ == "__main__":
    run_all()
