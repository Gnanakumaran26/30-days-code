print("📚 Library Management System - Day 27")

library = []

while True:
    print("\n1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Delete Book")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        year = input("Enter published year: ")
        library.append({"title": title, "author": author, "year": year})
        print("✅ Book added successfully!")

    elif choice == "2":
        if not library:
            print("📭 No books in library.")
        else:
            print("\n📖 Library Books:")
            for i, book in enumerate(library, 1):
                print(f"{i}. {book['title']} by {book['author']} ({book['year']})")

    elif choice == "3":
        search = input("Enter title to search: ")
        found = [book for book in library if search.lower() in book["title"].lower()]
        if found:
            for book in found:
                print(f"🔎 Found: {book['title']} by {book['author']} ({book['year']})")
        else:
            print("❌ No book found with that title.")

    elif choice == "4":
        title = input("Enter book title to delete: ")
        library = [book for book in library if book["title"].lower() != title.lower()]
        print("🗑️ Book deleted (if it existed).")

    elif choice == "5":
        print("👋 Exiting Library System...")
        break

    else:
        print("❌ Invalid choice. Try again.")
