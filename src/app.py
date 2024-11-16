import sqlite3

conn = sqlite3.connect('chocolate_house.db')
cursor = conn.cursor()

# Table creation
cursor.execute('CREATE TABLE IF NOT EXISTS seasonal_flavours (id INTEGER PRIMARY KEY, flavour_name TEXT NOT NULL, season TEXT NOT NULL)')

cursor.execute('CREATE TABLE IF NOT EXISTS ingredient_inventory (id INTEGER PRIMARY KEY, ingredient_name TEXT NOT NULL, quantity INTEGER NOT NULL, unit TEXT NOT NULL)')

cursor.execute('CREATE TABLE IF NOT EXISTS customer_suggestions (id INTEGER PRIMARY KEY,customer_name TEXT NOT NULL,suggested_flavour TEXT NOT NULL,allergy_concern TEXT)')

def add_seasonal_flavour(flavour_name, season):
    cursor.execute('INSERT INTO seasonal_flavours (flavour_name, season) VALUES (?, ?)', (flavour_name, season))
    conn.commit()
    print("Seasonal flavour added!")

def add_ingredient(ingredient_name, quantity, unit):
    cursor.execute('INSERT INTO ingredient_inventory (ingredient_name, quantity, unit) VALUES (?, ?, ?)', 
                   (ingredient_name, quantity, unit))
    conn.commit()
    print("Ingredient added!")

def add_customer_suggestion(customer_name, suggested_flavour, allergy_concern):
    cursor.execute('INSERT INTO customer_suggestions (customer_name, suggested_flavour, allergy_concern) VALUES (?, ?, ?)', 
                   (customer_name, suggested_flavour, allergy_concern))
    conn.commit()
    print("Customer suggestion added!")

def view_table_data(table_no):
    if table_no == '1':
        table = 'seasonal_flavours'
    elif table_no == '2':
        table = 'ingredient_inventory'
    elif table_no == '3':
        table = 'customer_suggestions'
    
    cursor.execute(f'SELECT * FROM {table}')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def main():
    while True:
        print()
        print("Chocolate House Management")
        print("1. Add a Seasonal flavour")
        print("2. Add an Ingredient to Inventory")
        print("3. Add a Customer Suggestion")
        print("4. View Data")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            flavour_name = input("Enter flavour name: ")
            season = input("Enter season (e.g., sumer, winter): ")
            add_seasonal_flavour(flavour_name, season)

        elif choice == '2':
            ingredient_name = input("Enter ingredient name: ")
            quantity = int(input("Enter quantity: "))
            unit = input("Enter unit (e.g., kg, liters): ")
            add_ingredient(ingredient_name, quantity, unit)

        elif choice == '3':
            customer_name = input("Enter customer name: ")
            suggested_flavour = input("Enter suggested flavour: ")
            allergy_concern = input("Enter allergy concern (or leave blank if none): ")
            add_customer_suggestion(customer_name, suggested_flavour, allergy_concern)

        elif choice == '4':
            table_no = input('''Enter table number to view 
            1.seasonal_flavours 
            2.ingredient_inventory 
            3.customer_suggestions 
            ''')
            if table_no in ('1','2','3'):
                view_table_data(table_no)
            else:
                print("invalid option")

        elif choice == '5':
            print("Exiting.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()

#sql close connection
conn.close()
