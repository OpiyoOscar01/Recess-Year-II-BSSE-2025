# Initial inventory
inventory = {
    "Apples": 50,
    "Bananas": 30,
    "Oranges": 20
}

def display_inventory():
    print("\nCurrent Inventory:")
    for item, qty in inventory.items():
        print(f"- {item}: {qty} units")

def add_stock():
    item = input("Enter item name to add: ").title()
    qty = int(input(f"Enter quantity to add to {item}: "))
    if item in inventory:
        inventory[item] += qty
    else:
        inventory[item] = qty
    print(f"{qty} units added to {item}.")

def remove_stock():
    item = input("Enter item name to remove: ").title()
    if item in inventory:
        qty = int(input(f"Enter quantity to remove from {item}: "))
        if qty <= inventory[item]:
            inventory[item] -= qty
            print(f"{qty} units removed from {item}.")
        else:
            print(f"Not enough stock to remove {qty} units.")
    else:
        print("Item not found in inventory.")

# Main loop
while True:
    print("\n=== Inventory Management ===")
    print("1. View Inventory")
    print("2. Add Stock")
    print("3. Remove Stock")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        display_inventory()
    elif choice == "2":
        add_stock()
    elif choice == "3":
        remove_stock()
    elif choice == "4":
        print("Exiting program...")
        break
    else:
        print("Invalid option. Please choose between 1 and 4.")
