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
    

# Auslesen der kompletten Einkaufsliste
def show_item():
    try:
        cursor.execute('SELECT * FROM groceries')
        items = cursor.fetchall()
    except sqlite3.Error as e:
        print(f'Failed to fetch a new record: {e}')
        
    # Anzeige von Artikeln in der Konsole    
    for item in items:
        print(item)

# Bearbeiten des Eintrags auf der Einkaufsliste
def update_item(id, name, amount, price):
    try:
        cursor.execute('''UPDATE groceries SET name = ?, amount = ?, price = ?
                   WHERE id = ? ''', (name, amount, price, id))
        conn.commit()
        print(f"Row with id {id} updated")
    except sqlite3.Error as e:
        print(f'Failed to update the item with id {id} {e}')
        
# Zum Löschen des Eintrags aus der Einkaufsliste       
def delete_item(id):
    try:
        cursor.execute('''
                   DELETE FROM groceries WHERE id = ?''', (id,))
        conn.commit()
        print (f"Item with id {id} deleted")
        
    except sqlite3.Error as e:
        print(f'Failed to delete the item with id {id} {e}')
        
        
def main():
    while True:
        print('<<<<<<<<<<-----Einkaufsliste----->>>>>>>>>>')
        print('1. Artikel hinzufügen')
        print('2. Artikel anzeigen')
        print('3. Artikel aktualisieren')
        print('4. Artikel löschen')
        print('5. Program beenden')
        
        choice = input('Bitte wähle eine Option {1, 2, 3, 4, oder 5}: ')
        
        match choice:
            case '1':
                print('Bitte gib die Daten des neuen Artikel ein: ')
                name = input('name: ')
                amount = input('amount: ')
                price = input('price: ')
                add_item(name, amount, price)
            case '2':
                show_item()
            case '3':
                print('Bitte gib die aktualisierten Daten ein: ')
                id = input("id: ")
                name = input('name: ')
                amount = input('amount: ')
                price = input('price: ')
                update_item(id, name, amount, price)
            case '4':
                print('Bitte gib die ID des zu löschonden Artikel: ')
                id = input('id: ')
                delete_item(id)
            case '5':
                print('Programm wird beended, Auf Wiedersehen')
                break
            case _:
                print('Ungültige Eingabe! Bitte wähle 1, 2, 3, 4, oder 5.')
                
if __name__  == '__main__':
    main()
        
        



    
