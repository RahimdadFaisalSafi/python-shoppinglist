shoppinglist = []

# shoppinglist.py

# List to store shopping items
shoppinglist = []

# Function to add an item to the shopping list
def add_item():
    # Ask the user for an item
    item = input("Bitte gib den Artikel ein, der zur Einkaufsliste hinzugefügt werden soll: ")
    # Add the item to the shopping list
    shoppinglist.append(item)
    # Print a confirmation message
    print(f"{item} wurde der Einkaufsliste hinzugefügt.")

# Call the function to test
add_item()
