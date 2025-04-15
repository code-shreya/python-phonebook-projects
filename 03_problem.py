phonebook = {}

def add_contact():
    name = input("Enter the name of the contact: ")
    primary_phone_number = input("Enter the primary contact number: ")
    secondary_phone_number = input("Enter the secondary contact number: ")
    email = input("Enter the email address: ")
    address = input("Enter the address: ")
    instagram_URL = input("Enter the Instagram URL: ")
    linkedIn_URL = input("Enter the LinkedIn URL: ")

    phonebook[name] = {
        "primary_phone_number": primary_phone_number,
        "secondary_phone_number": secondary_phone_number,
        "email": email,
        "address": address,
        "socials": {
            "instagram": instagram_URL,
            "linkedin": linkedIn_URL
        }
    }
    print(f"\n✅ Contact '{name}' added successfully!")

def view_all_contacts():
    if not phonebook:
        print("\n📭 Phonebook is empty.")
        return

    print("\n📘 All Contacts:")
    for name, details in phonebook.items():
        print(f"\nContact Name: {name}")
        print(f"Primary Phone: {details['primary_phone_number']}")
        print(f"Secondary Phone: {details['secondary_phone_number']}")
        print(f"Email: {details['email']}")
        print(f"Address: {details['address']}")
        print("Socials:")
        print(f"  Instagram: {details['socials']['instagram']}")
        print(f"  LinkedIn: {details['socials']['linkedin']}")

def search_contact():
    search_name = input("Enter the name to search: ")
    if search_name in phonebook:
        details = phonebook[search_name]
        print(f"\n🔍 Contact Found: {search_name}")
        print(f"Primary Phone: {details['primary_phone_number']}")
        print(f"Secondary Phone: {details['secondary_phone_number']}")
        print(f"Email: {details['email']}")
        print(f"Address: {details['address']}")
        print("Socials:")
        print(f"  Instagram: {details['socials']['instagram']}")
        print(f"  LinkedIn: {details['socials']['linkedin']}")
    else:
        print(f"\n❌ No contact found with the name '{search_name}'.")

# Main menu loop
while True:
    print("\n📱 Phonebook Menu:")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Choose an option (1–4): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_all_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        print("\n👋 Exiting Phonebook. Goodbye!")
        break
    else:
        print("❗ Invalid choice. Please try again.")
