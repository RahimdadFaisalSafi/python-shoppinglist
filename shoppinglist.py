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

# Aufruf der Funktion, um die Tabelle zu erstellen        
create_table()

# Hinzufügen eines neuen Lebensmittels
def add_item(name, amount, price):
    try:
        cursor.execute('''INSERT INTO groceries (name, amount, price) VALUES (?, ?, ?)''', (name, amount, price))
        conn.commit()
        print(f"{name} wurde hinzugefügt")
    except sqlite3.Error as e:
        print(f'Failed to add a new record: {e}')
    
# Aufruf der Funktion, um einen Studenten hinzuzufügen
add_item('Milch', '2 Packung', 2)




    

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
