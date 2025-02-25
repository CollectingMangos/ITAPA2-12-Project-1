import sqlite3

class Store:
    def __init__(self, db_name="store_database.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS products(
                product_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                product_name TEXT NOT NULL,
                product_price REAL NOT NULL,
                product_quantity INTEGER NOT NULL
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS sales(
                sales_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                product_ID INTEGER REFERENCES products(product_ID),
                sale_date TEXT NOT NULL,
                quantity_sold INTEGER NOT NULL,
                sale_total REAL NOT NULL
            )
        """)
        self.connection.commit()

    def add_product(self, product_name, product_price, product_quantity):
        if product_quantity <= 0:
            print("Product quantity must be greater than 0!")
            return
        self.cursor.execute("SELECT product_name FROM products WHERE product_name = ?", (product_name,))
        if self.cursor.fetchone():
            print("Product name already exists! Please use a different name.")
            return
        self.cursor.execute(
            "INSERT INTO products (product_name, product_price, product_quantity) VALUES (?, ?, ?)",
            (product_name, product_price, product_quantity)
        )
        self.connection.commit()
        print("Product added successfully!")
    
    def remove_product(self, product_id):
        self.cursor.execute("SELECT product_ID FROM products WHERE product_ID = ?", (product_id,))
        if self.cursor.fetchone():
            self.cursor.execute("DELETE FROM products WHERE product_ID = ?", (product_id,))
            self.connection.commit()
            print("Product removed successfully!")
        else:
            print("Product ID does not exist!")
    
    def update_product(self, product_id, new_product_name, new_product_price, new_product_quantity):
        self.cursor.execute("SELECT product_ID FROM products WHERE product_ID = ?", (product_id,))
        if self.cursor.fetchone():
            self.cursor.execute(
                "UPDATE products SET product_name=?, product_price=?, product_quantity=? WHERE product_ID=?",
                (new_product_name, new_product_price, new_product_quantity, product_id)
            )
            self.connection.commit()
            print("Product updated successfully!")
        else:
            print("Product ID does not exist! View all products to get the correct product ID.")
    
    def display_products(self):
        self.cursor.execute("SELECT * FROM products")
        products = self.cursor.fetchall()
        if products:
            print("\n{:<12} | {:<20} | {:<12} | {:<15}".format("Product ID", "Product Name", "Product Price", "Product Quantity"))
            print("----------------------------------------------------------------------")
            for row in products:
                print("{:<12} | {:<20} | R{:<12.2f} | {:<15}".format(row[0], row[1], row[2], row[3]))
        else:
            print("No products available. Please add some products!")
    
    def sell_product(self, product_id, sale_date, quantity):
        self.cursor.execute("SELECT product_quantity, product_price FROM products WHERE product_ID = ?", (product_id,))
        result = self.cursor.fetchone()
        if result:
            if result[0] >= quantity:
                new_quantity = result[0] - quantity
                sale_total = result[1] * quantity
                self.cursor.execute("UPDATE products SET product_quantity = ? WHERE product_ID = ?", (new_quantity, product_id))
                self.cursor.execute(
                    "INSERT INTO sales (product_ID, sale_date, quantity_sold, sale_total) VALUES (?, ?, ?, ?)",
                    (product_id, sale_date, quantity, sale_total)
                )
                self.connection.commit()
                print("Product sold successfully!")
            else:
                print("Not enough stock available!")
        else:
            print("Product ID does not exist! View all products to sell the correct item.")

    def close_connection(self):
        self.connection.close()

def main():
    store = Store()

    while True:
        print("\nWelcome to BE.2022.V6T6C1's Store Management System!")
        print("________________________________________")
        print("\n1. Add a product")
        print("2. Remove a product")
        print("3. Update a product")
        print("4. Display all products")
        print("5. Sell a product")
        print("0. Exit\n")

        choice = int(input("Select an option: "))

        if choice == 1:
            product_name = input("Enter product name: ")
            product_price = float(input("Enter the product's price: R"))
            product_quantity = int(input("Enter the product's quantity: "))
            store.add_product(product_name, product_price, product_quantity)
        elif choice == 2:
            product_id = int(input("Enter the product ID to remove: "))
            store.remove_product(product_id)
        elif choice == 3:
            product_id = int(input("Enter the product ID to update: "))
            new_product_name = input("Enter the new product name: ")
            new_product_price = float(input("Enter the new product price: R"))
            new_product_quantity = int(input("Enter the new product quantity: "))
            store.update_product(product_id, new_product_name, new_product_price, new_product_quantity)
        elif choice == 4:
            store.display_products()
        elif choice == 5:
            product_id = int(input("Enter the product ID to sell: "))
            sale_date = input("Enter the sale date with format DD/MM/YYYY: ")
            quantity = int(input("Enter the quantity to sell: "))
            store.sell_product(product_id, sale_date, quantity)
        elif choice == 0:
            print("Cheers!")
            store.close_connection()
            break
        else:
            print("Please select a valid option.")

if __name__ == "__main__":
    main()