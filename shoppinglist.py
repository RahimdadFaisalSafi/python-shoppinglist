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
    
# Aufruf der Funktion, um ein Lebensmittels hinzuzufügen
add_item('Milch', '2 Packung', 2)

# Auslesen der kompletten Einkaufsliste
def show_item():
    try:
        cursor.execute('SELECT * FROM groceries')
        items = cursor.fetchall()
    except sqlite3.Error as e:
        print(f'Failed to fetch a new record: {e}')
        
    for item in items:
        print(item)
        
show_item()



    
