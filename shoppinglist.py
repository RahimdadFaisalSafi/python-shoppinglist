import sqlite3

# Verbindung zu SQLite (Falls nicht vorhanden, dann wird erstellt)
conn = sqlite3.connect('shoppinglist.db')

# Erstellung von cursor object, um SQL-Befehl durchzuführen
cursor = conn.cursor()

# Erstellung von Tabellen in shoppinglist.db mit der richtegen Spalte.
def create_table():
    try:
        cursor.execute('''CREATE TABLE IF NOT EXISTS groceries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(32),
        amount VARCHAR(32),
        price INTEGER
    
        )''')
        conn.commit()
    except sqlite3.Error as e:
        print(e)
create_table()

# # List to store shopping items
# shoppinglist = []

# # Function to add an item to the shopping list
# def add_item():
#     # Ask the user for an item
#     item = input("Bitte gib den Artikel ein, der zur Einkaufsliste hinzugefügt werden soll: ")
#     # Add the item to the shopping list
#     shoppinglist.append(item)
#     # Print a confirmation message
#     print(f"{item} wurde der Einkaufsliste hinzugefügt.")

# # Call the function to test
# add_item()
