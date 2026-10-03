inventory = {
    "keyboard": 5,
    "mouse": 8,
    "monitor": 3,
    "laptop": 4
}
def display_inventory():
    print("\n==== INVENTORY ====\n")
    for key in inventory:
        print(f"{key}: {inventory[key]}")

def check_item():
    item = input("Enter item to check: ")
    if item in inventory:
        print(f"{item} is available.")
        print(f"Quantity: {inventory[item]}")
    else:
        print(f"{item} is not in the inventory")
def add_item():
    add = input("Do you want to add an item? (yes/no): ")
    def update_quantity():
        quantity = int(input("Quantity: "))
        inventory[item_name] = quantity
    if add == "yes":
        item_name = input("Item name: ")
        if item_name in inventory:
            decision = input("Item already exists, do you want to update it? (yes/no): ")
            if decision == "yes":
                update_quantity()
            elif decision == "no":
                print("No changes made!")
        else:
            update_quantity()
        display_inventory()
def update_dict():
    update = (input("What do you want to update?: "))
    if update in inventory:
        new_value = int(input("Enter new value: "))
        inventory[update] = new_value
        display_inventory()
    else:
        print("Item does not exist!")
while True:
    choice = input("\nWelcome :) what do you want to do?\n1.Display Everything\n2.Search\n3.Add\n4.Update\n5.Exit\n>>>")
    if choice == "1":
        display_inventory()
    elif choice == "2":
        check_item()
    elif choice == "3":
        add_item()
    elif choice == "4":
        update_dict()
    elif choice == "5":
        break
    else:
        print("Please select a valid option!")


