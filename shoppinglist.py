# shoppinglist.py
shoppinglist = []


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

# Function to show the shopping list
def show_shoppinglist():
    # Check if the shopping list is empty
    if shoppinglist:
        print("Deine Einkaufsliste:")
        # Use a for loop to print each item from the shopping list
        for item in shoppinglist:
            print(f"- {item}")
    else:
        print("Deine Einkaufsliste ist leer.")

# Test the functions
add_item()  
show_shoppinglist()  