print("📖 Contact Book - Day 10")

contacts = {}

def add_contact():
    name = input("Enter name: ").title()
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    contacts[name] = {"phone": phone, "email": email}
    print(f"✅ {name} added successfully!")

def view_contacts():
    if not contacts:
        print("❌ No contacts found.")
    else:
        print("\n📒 Your Contacts:")
        for name, info in contacts.items():
            print(f"{name} - 📞 {info['phone']} | ✉️ {info['email']}")

def search_contact():
    name = input("Enter name to search: ").title()
    if name in contacts:
        info = contacts[name]
        print(f"🔍 {name} - 📞 {info['phone']} | ✉️ {info['email']}")
    else:
        print("❌ Contact not found.")

def delete_contact():
    name = input("Enter name to delete: ").title()
    if name in contacts:
        del contacts[name]
        print(f"🗑️ {name} deleted successfully!")
    else:
        print("❌ Contact not found.")

while True:
    print("\nOptions: add | view | search | delete | exit")
    choice = input("Choose: ").lower()

    if choice == "add":
        add_contact()
    elif choice == "view":
        view_contacts()
    elif choice == "search":
        search_contact()
    elif choice == "delete":
        delete_contact()
    elif choice == "exit":
        print("👋 Exiting Contact Book...")
        break
    else:
        print("❌ Invalid option, try again.")
