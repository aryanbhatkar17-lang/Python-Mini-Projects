import csv
import os

inventory = {}

def load_inventory():
    if os.path.exists("inventory.csv"):
        if os.path.getsize("inventory.csv") == 0:
            print("inventory.csv is empty. Starting with a fresh inventory!\n")
            return

        with open("inventory.csv", "r") as file:
            reader = csv.reader(file)
            try:
                next(reader) 
                
                rows_loaded = 0
                for row in reader:
                    if row: 
                        name, quantity, price = row
                        inventory[name] = [int(quantity), float(price)]
                        rows_loaded += 1
                
                if rows_loaded > 0:
                    print(f"✅ Data loaded successfully! ({rows_loaded} products imported)\n\n")
                    view_inventory()
                else:
                    print("ℹ️ File contains headers but no data. Starting fresh!\n")

            except StopIteration:
                print("inventory.csv is empty. Starting with a fresh inventory!\n")

def add_product():
    name = input("Enter product name: ").strip().upper()
    quantity = get_numeric_input("Enter product quantity: ", False)
    price = get_numeric_input("Enter price per unit: ", True)

    if name in inventory:
        inventory[name][0] += quantity
    else:
        inventory[name] = [quantity, price]
    print(f"Product {name} added successfully!\n")


def view_inventory():
    if not inventory:
        print("Empty inventory")
        return

    print("Current inventory:")
    print(f"{'NAME':<20} | {'QUANTITY':<10} | {'PRICE':<10}")
    print("-" * 48)
    for name, details in inventory.items():
        print(f"{name:<20} | {details[0]:<10} | ${details[1]:.2f}")
    print()


def update_stock():
    name = input("Enter product name to be updated: ").strip().upper()
    if name in inventory:
        quantity = int(input("Enter new quantity: "))
        inventory[name][0] = quantity
        print(f"Updated {name} stock to {quantity}\n")
    else:
        print("Product not found!\n")


def delete_product():
    name = input("Enter product which is to be removed: ").strip().upper()
    if name in inventory:
        del inventory[name]
        print(f"Product - {name} has been removed from the inventory")
    else:
        print(f"No '{name}' such product found")


def search_product():
    name = input("Enter product name to search: ").strip().upper()
    if name in inventory:
        print(f"{name}: Quantity={inventory[name][0]}, Price=${inventory[name][1]:.2f}\n")
    else:
        print("Product not found!\n")


def save_inventory():
    with open("inventory.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Product Name", "Quantity", "Price"])
        for name, details in inventory.items():
            writer.writerow([name, details[0], details[1]])
    print("Inventory saved to inventory.csv\n")

def low_stock_check():
    threshold = 5  # Alert if stock drops below 5
    low_stock_items = [name for name, details in inventory.items() if details[0] < threshold]
    
    if low_stock_items:
        print("----------------------")
        print("⚠️ LOW STOCK ALERT:")
        print("----------------------")
        for name in low_stock_items:
            print(f"  - {name} has only {inventory[name][0]} left!")


def view_total_value():
    if not inventory:
        print("Inventory is empty. Total Value: $0.00\n")
        return
        
    total_value = sum(details[0] * details[1] for details in inventory.values())
    print("-----------------------------------\n")
    print(f"Total Portfolio Value: ${total_value:,.2f}\n")
    print("-----------------------------------\n")


def get_numeric_input(prompt, is_float=False):
    while True:
        try:
            if is_float:
                return float(input(prompt))
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.\n")

    
if __name__ == "__main__":

    load_inventory()

    while(True):
        print("1. Add Product\n2. View Inventory\n3. Update Stock\n4. Delete Product\n5. Search Product\n6. View Total Value\n7. Save & Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_product()
        elif choice == "2":
            view_inventory()
        elif choice == "3":
            update_stock()
        elif choice == "4":
            delete_product()
        elif choice == "5":
            search_product()
        elif choice == "6":
            view_total_value()
        elif choice == "7":
            save_inventory()
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.\n")

        low_stock_check()