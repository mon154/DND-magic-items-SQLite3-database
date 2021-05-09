# Sprint One
# Name: Keyanna Oliphant
# Description: Command line SQLite program that creates and pulls data from a DND magic items database (I enter magic items listed here https://donjon.bin.sh/5e/magic_items/ because
# DNDBeyond requires you to own the book the item is in to view the items so it's harder to copy the text and I don't feel like buying $800 worth of dnd sourcebooks lol :P)

#imports the library and establishes the connection
import sqlite3
connection = sqlite3.connect('items.db')
cursor = connection.cursor()

def create_database(): #Creates the starter tables and prints the tables in the database
    '''
    Items Table
    cursor.execute("CREATE TABLE items (item_id, name, rarity, type, attunement)")
    items =  [(1,"Absorbing Tattoo", 9, 1, "Y"), (2, "Adamantite Armor", 2, 1, 'No')]
    cursor.executemany("INSERT INTO items VALUES (?,?,?,?,?)", items)
    connection.commit()

    Rarity Table
    cursor.execute("CREATE TABLE rarity (rarity_id, name)")
    items =  [(1, "Common"), (2, "Uncommon"), (3, "Rare"), (4, "Very Rare"), (5, "Legendary"), (6, "Artifact")]
    cursor.executemany("INSERT INTO rarity VALUES (?,?)", items)
    connection.commit()

    Type Table
    cursor.execute("CREATE TABLE type (type_id, name)")
    items =  [(1, "Armor"), (2, "Potion"), (3, "Ring"), (4, "Rod"), (5, "Scroll"), (6, "Staff"), (7, "Wand"), (8, "Weapon"), (9, "Wondrous Item")]
    cursor.executemany("INSERT INTO rarity VALUES (?,?)", items)
    connection.commit()
    
    #checking that tables exist
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print(cursor.fetchall())
    '''
def run_user_program(): #Runs the main program on a while loop that will keep going until the user either quits from the menu or chooses to not continue using the program after 
    #finishing or causing an error in one of the options. Gives the user the ability to add, search, modify, delete, items, or display the items table.
    print("")
    print("Welcome to our D&D magic items database!")
    print("Please enter all inputs as integers unless otherwise specified")
    program_continue = True
    while program_continue == True:
        print("")
        print_menu()
        entry = input("Select what you would like to do: ")
        if entry == "1":
            program_continue = add_item()
        elif entry == "2":
            program_continue = search_items()
        elif entry == "3":
            program_continue = modify_item()
        elif entry == "4":
            program_continue = delete_item()
        elif entry == "5":
            program_continue = display_items()
        elif entry == "6":
            program_continue = False
        else:
            print("Invalid input, please enter an integer between 1 and 6.")
            program_continue = True
    print("Thank you for using our program, have a nice day.")
    print("")

def print_menu():
    print("1. Add Item to Database")
    print("2. Search for Item(s) in Database")
    print("3. Modify Item in Database")
    print("4. Delete Item in Database")
    print("5. Display items table")
    print("6. Exit Program")

def check_item_exists(name):
    name = name
    if cursor.execute("SELECT * FROM items WHERE name = ?", (name,)).fetchone():
        item_exists = True
    else:
        item_exists = False
    return item_exists 

def program_continue():
    program_continue = input("Would you like to continue using the program?(Yes or No, case sensitive) ")
    if program_continue == "Yes":
        program_continue = True
        return program_continue
    elif program_continue == "No":
        program_continue = False
        return program_continue
    else:
        print("We didn't understand your input so we're taking you back to the main menu")
        program_continue = True
        return program_continue

def add_item():
    #gets the current highest item id and adds one to get the new item id
    cursor.execute("SELECT * FROM items ORDER BY item_id DESC LIMIT 1")
    for record in cursor.fetchall():
        current_id = record[0]
    new_id = current_id + 1
    #gets the name of the item
    name = input("Enter the name of the item you would like to add.(Please capitalize the first letter of every word) ")
    #checks if item is already in database
    exists = check_item_exists(name)
    if exists == True:
        print("This item is already in our database.")
    else:
        #gets the rarity of the item
        print("Our current rarities are 1. Common, 2. Uncommon, 3. Rare, 4. Very Rare, 5. Legendary, and 6. Artifact.")
        rarity = input("What is the rarity of the item?(Please enter an integer between 1 and 6) ")
        print("")
        #gets the type of the item
        print("Our current types are 1. Armor, 2. Potion, 3. Ring, 4. Rod, 5. Scroll, 6. Staff, 7. Wand, 8. Weapon, and 9. Wondrous Item")
        item_type = input("What is the item's type?(Please enter an integer between 1 and 9) ")
        print("")
        #gets the attunement of the item
        attunement = input("Does this item require attunement?(Please enter Y or No) " )
    
        values = (new_id, name, rarity, item_type, attunement)
        cursor.execute("INSERT INTO items VALUES (?,?,?,?,?)", values)
        connection.commit()

    program_c = program_continue()
    return program_c

def search_items():
    print("")
    print("Search Parameters:")
    print("1. Name")
    print("2. Rarity")
    print("3. Type")
    print("4. Attunement")
    parameter = input("What parameter do you want to search by? ")

    if parameter == "1":
        search_by_name()
    elif parameter == "2":
        search_by_rarity()
    elif parameter == "3":
        search_by_type()
    elif parameter == "4":
        search_by_attunement()

    program_c = program_continue()
    return program_c

def search_by_name():
    name = input("What is the name of the item? ")
    exists = check_item_exists(name)
    if exists == True:
        #cursor.execute("SELECT items.name, rarity.name, items.type, items.attunement FROM items INNER JOIN rarity ON items.rarity == rarity.rarity_id WHERE items.name == ?", (name,))
        cursor.execute("SELECT name, rarity, type, attunement FROM items WHERE name == ?", (name,))
        print("{:>10}  {:>10}  {:>10}  {:>10}".format("Item Name", "Rarity", "Type", "Attunement"))
        for record in cursor.fetchall():
            print("{:>10}  {:>10}  {:>10}  {:>10}".format(record[0], record[1], record[2], record[3]))
    elif exists == False:
        print("This item doesn't appear to be in the database yet, either double check the spelling and try again or feel free to add the item to our database.")
    else:
        print("I don't know how you managed to break the code, good job. You'll probably need to restart the program now")

def search_by_rarity():
    print("Our current rarities are 1. Common, 2. Uncommon, 3. Rare, 4. Very Rare, 5. Legendary, and 6. Artifact.")
    rarity = input("Which rarity would you like to see?(Please select integer between 1 and 6) ")
    #if cursor.execute("SELECT items.name, rarity.name, type.name, items.attunement FROM items LEFT JOIN rarity ON items.rarity == rarity.rarity_id LEFT JOIN type ON items.type == type.type_id  WHERE items.rarity = ?", (rarity,)).fetchall():
        #print("This worked")
    #else:
        #print("This didn't work")
    #cursor.execute("SELECT items.name, rarity.name, type.name, items.attunement FROM items LEFT JOIN rarity ON items.rarity == rarity.rarity_id LEFT JOIN type ON items.type == type.type_id  WHERE items.rarity = ?", (rarity,))
    cursor.execute("SELECT name, rarity, type, attunement FROM items WHERE rarity == ?", (rarity,))
    print("{:>10}  {:>10}  {:>10}  {:>10}".format("Item Name", "Rarity", "Type", "Attunement"))
    for record in cursor.fetchall():
        print("{:>10}  {:>10}  {:>10}  {:>10}".format(record[0], record[1], record[2], record[3]))
def search_by_type():
    print("Our current types are 1. Armor, 2. Potion, 3. Ring, 4. Rod, 5. Scroll, 6. Staff, 7. Wand, 8. Weapon, and 9. Wondrous Item")
    item_type = input("Which type would you like to see?(Please select integer between 1 and 9) ")
    #cursor.execute("SELECT items.name, rarity.name, type.name, items.attunement FROM items INNER JOIN rarity ON items.rarity == rarity.rarity_id INNER JOIN type ON items.type == type.type_id  WHERE items.type = ?", (item_type,))
    cursor.execute("SELECT name, rarity, type, attunement FROM items WHERE type == ?", (item_type,))
    print("{:>10}  {:>10}  {:>10}  {:>10}".format("Item Name", "Rarity", "Type", "Attunement"))
    for record in cursor.fetchall():
        print("{:>10}  {:>10}  {:>10}  {:>10}".format(record[0], record[1], record[2], record[3]))
def search_by_attunement():
    attunement = input("Do you want to see items the require attunement? (Y or No, case sensitive) ")
    #cursor.execute("SELECT items.name, rarity.name, type.name, items.attunement FROM items INNER JOIN rarity ON items.rarity == rarity.rarity_id INNER JOIN type ON items.type == type.type_id  WHERE items.attunement = ?", (attunement,))
    cursor.execute("SELECT name, rarity, type, attunement FROM items WHERE attunement == ?", (attunement,))
    print("{:>10}  {:>10}  {:>10}  {:>10}".format("Item Name", "Rarity", "Type", "Attunement"))
    for record in cursor.fetchall():
        print("{:>10}  {:>10}  {:>10}  {:>10}".format(record[0], record[1], record[2], record[3]))

def modify_item():
    name = input("Please enter the name of the item you would like to modify.(Please capitalize the first letter of every word) ")
    exists = check_item_exists(name)
    if exists == True:
        pass
    else:
        print("This item isn't in our database yet. You can add it from the main menu if you would like.")
    print("")
    print("The traits you can modify are 1. Name, 2. Rarity, 3. Type, or 4. Attunement")
    modify_trait = input("What trait do you want to modify?(Please enter an integer between 1 and 4) ")
    if modify_trait == "1":
        new_name = input("what would you like to change the name to? ")
        values = (new_name, name)

        cursor.execute("UPDATE items SET name = ? WHERE name = ?", values)
        connection.commit()
    elif modify_trait == "2":
        print("Our current rarities are 1. Common, 2. Uncommon, 3. Rare, 4. Very Rare, 5. Legendary, and 6. Artifact.")
        new_rarity = input("what would you like to change the rarity to?(Please enter an integer between 1 and 6) ")
        values = (new_rarity, name)

        cursor.execute("UPDATE items SET rarity = ? WHERE name = ?", values)
        connection.commit()
    elif modify_trait == "3":
        print("Our current types are 1. Armor, 2. Potion, 3. Ring, 4. Rod, 5. Scroll, 6. Staff, 7. Wand, 8. Weapon, and 9. Wondrous Item")
        new_type = input("what would you like to change the type to?(Please enter an integer between 1 and 9) ")
        values = (new_type, name)

        cursor.execute("UPDATE items SET type = ? WHERE name = ?", values)
        connection.commit()
    elif modify_trait == "4":
        new_attunement = input("what would you like to change the attunement to?(Please enter either Y or No) ")
        values = (new_attunement, name)

        cursor.execute("UPDATE items SET attunement = ? WHERE name = ?", values)
        connection.commit()
    else:
        print("The trait you entered was invalid")

    program_c = program_continue()
    return program_c

def delete_item():
    name = input("What is the name of the item you would like to delete? (Please capitalize the first letter of every word) ")
    exists = check_item_exists(name)
    if exists == True:
        values = (name, )
        cursor.execute("DELETE FROM items WHERE name = ?", values)
        connection.commit()
    else:
        print("This item currently isn't in our database.")

    program_c = program_continue()
    return program_c

def display_items():
    cursor.execute("SELECT * FROM items")
    print("{:>10}  {:>10}  {:>10}  {:>10}  {:>10}".format("ID", "Name", "Rarity", "Type", "Attunement"))
    for record in cursor.fetchall():
        print("{:>10}  {:>10}  {:>10}  {:>10}  {:>10}".format(record[0], record[1], record[2], record[3], record[4]))
    
    program_c = program_continue()
    return program_c

def main():
    create_database() #Only a one time function to create the database so it won't do anything unless the code in the function is uncommented
    run_user_program() #Calls the run_user_program function (see function description)

if __name__ == "__main__":
    main()

#example item
#Alchemical Compendium
#Rare
#Wondrous Item
#Y