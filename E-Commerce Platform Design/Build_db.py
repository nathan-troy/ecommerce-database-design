import sqlite3
import os
import random

#Locate the workspace directory
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DB_FILE = os.path.join(SCRIPT_DIR, "nexusmart.db")

#Relational schema definition
SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS Users (
    UserID INTEGER PRIMARY KEY AUTOINCREMENT,
    AddressLine1 VARCHAR(50) NOT NULL,
    AddressLine2 VARCHAR(50),
    FirstName VARCHAR(20) NOT NULL,
    Surname VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS Products (
    ProductID INTEGER PRIMARY KEY AUTOINCREMENT,
    ProductName VARCHAR(30) NOT NULL,
    ProductPrice DECIMAL(10, 2) NOT NULL,
    DistributorName VARCHAR(30) NOT NULL
);

CREATE TABLE IF NOT EXISTS UserTransactions (
    TransactionID INTEGER PRIMARY KEY AUTOINCREMENT,
    Amount DECIMAL(10, 2) NOT NULL,
    TransactionType VARCHAR(20) NOT NULL CHECK (TransactionType IN ('Deposit', 'Purchase', 'Refund')),
    Timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UserID INT NOT NULL REFERENCES Users(UserID) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Orders (
    OrderID INTEGER PRIMARY KEY AUTOINCREMENT,
    UserID INT NOT NULL REFERENCES Users(UserID) ON DELETE RESTRICT,
    DeliveryDate TIMESTAMP,
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS Order_items (
    OrderItemID INTEGER PRIMARY KEY AUTOINCREMENT,
    OrderID INT NOT NULL REFERENCES Orders(OrderID) ON DELETE RESTRICT,
    ProductID INT NOT NULL REFERENCES Products(ProductID) ON DELETE RESTRICT,
    PriceAtPurchase DECIMAL(10, 2) NOT NULL,
    Quantity INT NOT NULL CHECK (Quantity > 0)
);

CREATE TABLE IF NOT EXISTS InventoryLedger (
    InventoryID INTEGER PRIMARY KEY AUTOINCREMENT,
    ProductID INT NOT NULL REFERENCES Products(ProductID) ON DELETE RESTRICT,
    QuantityChange INT NOT NULL CHECK (QuantityChange <> 0),
    Reason VARCHAR(50) NOT NULL CHECK (Reason IN ('RESTOCK', 'SALE', 'DAMAGED', 'RETURN')),
    Timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS Cart_items (
    UserID INT NOT NULL REFERENCES Users(UserID) ON DELETE CASCADE,
    ProductID INT NOT NULL REFERENCES Products(ProductID) ON DELETE CASCADE,
    Quantity INT NOT NULL CHECK (Quantity > 0),
    TimeAdded TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (UserID, ProductID)
);
"""

def generate_and_seed_1000_users(cursor):
    #Generate mock users using internal lists to prevent file reading bugs
    print("Generating 1000 mock customer records programmatically...")
    first_names = ["Oliver", "George", "Noah", "Arthur", "Muhammad", "Leo", "Oscar", "Amelia", "Olivia", "Isla", "Ava", "Mia"]
    last_names = ["Smith", "Jones", "Taylor", "Brown", "Williams", "Wilson", "Johnson", "Davies", "Robinson", "Wright"]
    streets = ["High Street", "Station Road", "Main Street", "Park Road", "Church Lane", "London Road", "Victoria Road"]
    
    user_records = []
    for _ in range(1000):
        f_name = random.choice(first_names)
        l_name = random.choice(last_names)
        addr1 = f"{random.randint(1, 250)} {random.choice(streets)}"
        addr2 = f"Apt {random.randint(1, 20)}" if random.random() > 0.5 else None
        user_records.append((addr1, addr2, f_name, l_name))
        
    cursor.executemany(
        "INSERT INTO Users (AddressLine1, AddressLine2, FirstName, Surname) VALUES (?, ?, ?, ?);",
        user_records
    )
    print("Successfully injected 1000 customers into the Users table.")

def seed_complete_marketplace_ecosystem(cursor):
    #Automated routine to populate the remaining relational platform layers at scale
    print("Beginning master marketplace data injection pipeline...")

    #Seed a diverse tech catalog of 250 unique product variations
    distributors = ["Anker Wholesales", "OReilly Logistics", "Logitech Hub", "Amazon Bulk Shipping", "Intel Components", "Corsair Supply"]
    items = ["Mechanical Keyboard", "USB-C Hub", "4K Monitor", "Ergonomic Mouse", "Data Engineering Textbook", "Solid State Drive", "Graphics Card", "Desk Mat"]
    colors = ["Midnight Black", "Arctic White", "Space Grey", "Neon RGB", "Matte Blue", "Stealth Charcoal"]
    
    product_records = []
    for _ in range(250):
        name = f"{random.choice(colors)} {random.choice(items)} V{random.randint(1,5)}"
        price = round(random.uniform(10.00, 450.00), 2)
        distributor = random.choice(distributors)
        product_records.append((name, price, distributor))
        
    cursor.executemany(
        "INSERT INTO Products (ProductName, ProductPrice, DistributorName) VALUES (?, ?, ?);",
        product_records
    )
    print("Products Catalog Seeding Complete with 250 scaled items live.")

    #Seed base warehouse supplier stock levels for all 250 catalog products
    inventory_logs = []
    for product_id in range(1, 251):
        stock_quantity = random.randint(50, 500)
        inventory_logs.append((product_id, stock_quantity, 'RESTOCK'))
        
    cursor.executemany(
        "INSERT INTO InventoryLedger (ProductID, QuantityChange, Reason) VALUES (?, ?, ?);",
        inventory_logs
    )
    print("Warehouse Inventory Ledger Seeding Complete for all 250 products.")

    #Seed starter capital deposits for all 1000 programmatically generated users
    financial_logs = []
    for user_id in range(1, 1001):
        starting_cash = round(random.uniform(50.00, 2500.00), 2)
        financial_logs.append((starting_cash, 'Deposit', user_id))
        
    cursor.executemany(
        "INSERT INTO UserTransactions (Amount, TransactionType, UserID) VALUES (?, ?, ?);",
        financial_logs
    )
    print("Customer Financial Balance Seeding Complete for all 1000 active users.")

    #Seed 400 active unpurchased shopping baskets safely avoiding duplicate composite keys
    cart_records = set()
    while len(cart_records) < 400:
        rand_user = random.randint(1, 1000)
        rand_product = random.randint(1, 250)
        rand_quantity = random.randint(1, 4)
        cart_records.add((rand_user, rand_product, rand_quantity))
        
    cursor.executemany(
        "INSERT OR IGNORE INTO Cart_items (UserID, ProductID, Quantity) VALUES (?, ?, ?);",
        list(cart_records)
    )
    print("Active Shopping Cart State Seeding Complete with 400 distributed baskets.")


def actualise_database():
    try:
        #Establish local binary connection and activate foreign key checking
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("PRAGMA foreign_keys = ON;")
        print(f"Created empty database container: '{DB_FILE}'")

        #Run structural setup rules
        cursor.executescript(SCHEMA_SQL)
        print("Schema loaded and 7 tables verified successfully.")
        conn.commit()

        #Group operations into an isolated database transaction block
        cursor.execute("BEGIN TRANSACTION;")
        
        generate_and_seed_1000_users(cursor)
        seed_complete_marketplace_ecosystem(cursor)
        
        cursor.execute("COMMIT;")

        #Verify current live state row count
        cursor.execute("SELECT COUNT(*) FROM Users;")
        user_count = cursor.fetchone()[0]
        print(f"Success! System actualised. Users table holds {user_count} live rows.")

    except Exception as e:
        print(f"Critical Execution Failure: {e}")
        try:
            conn.rollback()
        except:
            pass
    finally:
        try:
            conn.close()
            print("Database connection closed.")
        except:
            pass

if __name__ == "__main__":
    actualise_database()

