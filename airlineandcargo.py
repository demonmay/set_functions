import csv

#list is created
ticket_fields = ['Ticket ID', 'Passenger Name', 'Flight Number', 'Departure', 'Destination', 'Status']
cargo_fields = ['Shipment ID', 'Shipper Name', 'Receiver Name', 'Origin', 'Destination', 'Status']

# File names for storing ticket and cargo records
ticket_database = 'airline_tickets.csv'
cargo_database = 'cargo_shipments.csv'

# Function to display menu options
def display_menu():
    print("--------------------------------------")
    print(" Welcome to Airline Ticket and Cargo Shipping Management System")
    print("---------------------------------------")
    print("1. Book Airline Ticket")
    print("2. View Airline Tickets")
    print("3. Search Airline Ticket")
    print("4. Book Cargo Shipment")
    print("5. View Cargo Shipments")
    print("6. Search Cargo Shipment")
    print("7. Quit")

# Function to book a new airline ticket
def book_airline_ticket():
    print("-----------------------------")
    print("Book New Airline Ticket")
    print("-----------------------------")

    ticket_data = []
    for field in ticket_fields:
        value = input("Enter " + field + ": ")
        ticket_data.append(value)

    with open(ticket_database, "a", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(ticket_data)

    print("Airline ticket booked successfully")
    input("Press any key to continue")

# Function to view existing airline tickets
def view_airline_tickets():
    print("--- Airline Ticket Records ---")

    with open(ticket_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for x in ticket_fields:
            print(x, end='\t |')
        print("\n-----------------------------------------------------------------")

        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")

    input("Press any key to continue")

# Function to search for an airline ticket
def search_airline_ticket():
    print("--- Search Airline Ticket ---")
    ticket_id = input("Enter Ticket ID to search: ")
    with open(ticket_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                if ticket_id == row[0]:
                    print("----- Airline Ticket Found -----")
                    for field, value in zip(ticket_fields, row):
                        print(field + ": " + value)
                    break
        else:
            print("Airline Ticket ID not found in our database")
    input("Press any key to continue")


# Function to book a new cargo shipment
def book_cargo_shipment():
    print("-----------------------------")
    print("Book New Cargo Shipment")
    print("-----------------------------")

    cargo_data = []
    for field in cargo_fields:
        value = input("Enter " + field + ": ")
        cargo_data.append(value)

    with open(cargo_database, "a", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(cargo_data)

    print("Cargo shipment booked successfully")
    input("Press any key to continue")

# Function to view existing cargo shipments
def view_cargo_shipments():
    print("--- Cargo Shipment Records ---")

    with open(cargo_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for x in cargo_fields:
            print(x, end='\t |')
        print("\n-----------------------------------------------------------------")

        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")

    input("Press any key to continue")

# Function to search for a cargo shipment
def search_cargo_shipment():
    print("--- Search Cargo Shipment ---")
    shipment_id = input("Enter Shipment ID to search: ")
    with open(cargo_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                if shipment_id == row[0]:
                    print("----- Cargo Shipment Found -----")
                    for field, value in zip(cargo_fields, row):
                        print(field + ": " + value)
                    break
        else:
            print("Cargo Shipment ID not found in our database")
    input("Press any key to continue")

# Function to update the status of a cargo shipment

# Main loop for menu selection
while True:
    display_menu()

    choice = input("Enter your choice: ")
    if choice == '1':
        book_airline_ticket()
    elif choice == '2':
        view_airline_tickets()
    elif choice == '3':
        search_airline_ticket()
    elif choice == '4':
        book_cargo_shipment()
    elif choice == '5':
        view_cargo_shipments()
    elif choice == '6':
        search_cargo_shipment()
    elif choice == '7':
        break

print("-------------------------------")
print(" Thank you for using our system")
print("-------------------------------")