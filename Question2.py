import sqlite3

# connection = sqlite3.connect("store_database.db")
# cursor = connection.cursor()

class Store:
    def __init__(self):
        pass
    
    def add_product(self, product_name, product_price, product_quantity):
        pass
    
    def remove_product(self, product_id):
        pass
    
    def update_product(self, product_id, new_product_name, new_product_price, new_product_quantity):
        pass
    
    def display_products(self):
        pass
    
    def sell_product(self, product_id, sale_date, quantity):
        pass

def main():
    # inventory = InventoryManagement()

    while True:
        print("\nWelcome to BE.2022.V6T6C1's Store Management System!")
        print("________________________________________")
        print("\n1. Add a prouct")
        print("2. Remove a prouct")
        print("3. Update a prouct")
        print("4. Display all proucts")
        print("5. Sell a prouct")
        print("0. Exit\n")

        choice = int(input("Select an option: "))

        if choice == 1:
            print("\nLet's add a product!")
            product_name = input("Enter product name: ")
            product_price = float(input("Enter the product's price: "))
            product_quantity = int(input("Enter the product's quantity: "))
            #  method for adding a product goes here
            # quantity cannot be 0
            print("Product added successfully!")
        elif choice == 2:
            product_id = int(input("Enter the product ID to remove: "))
            # remove a product method goes here
            print("Data deleted successfully!")
        elif choice == 3:
            product_id = int(input("Enter the product ID to update: "))
            new_product_name = input("Enter the new product name: ")
            new_product_price = float(input("Enter the new product price: "))
            new_product_quantity = int(input("Enter the new product quantity: "))
            # update a product method goes here
            #  add if statement here to check if the product exists in DB
            # check if new name is same as old and add an error message
            #  check if new price is same as old and add an error message
            print("Product updated successfully!")
        elif choice == 4:
            # display all products method goes here
            print("Displaying all products!")
        elif choice == 5:
            product_id = int(input("Enter the product ID to sell: "))
            sale_date = input("Enter the sale date with format DD/MM/YYY: ")
            quantity = int(input("Enter the quantity to sell: "))
            # sell a product method goes here
            # add if statements to check if quantity is 0 in the DB for quantity
            print("Product/s sold successfully!")
        elif choice == 0:
            print("Cheers!")
            break
        else:
            print("Please select a valid option.")

if __name__ == "__main__":
    main()