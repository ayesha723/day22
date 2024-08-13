contacts = [
    ("sara", "0011"),
    ("ali", "0022"),
    ("noor", "0033"),
    ("zain", "0044"),
    ("warda", "0055"),
    ("ayesha", "0066")
]

def view_contacts():
    print("Current Contacts:")
    for name, contact in contacts:
        print(f"{name}: {contact}")

def add_contact():
    name = input("Enter the name of the person: ").strip()
    contact = input("Enter the contact of the person: ").strip()

    global contacts
    # Check if the name already exists
    for item in contacts:
        if item[0] == name:
            print("Contact with this name already exists.")
            return
    
    contacts.append((name, contact))
    print("Contact saved successfully.")

def main():
    while True:
        print("Main Menu:")
        print("1. View Contacts")
        print("2. Add Contact")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == '1':
            view_contacts()
        elif choice == '2':
            add_contact()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()


