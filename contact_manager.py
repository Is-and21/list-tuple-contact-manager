# Contact manager application
contacts = []

while True:
    choice = input("\n1. Add\n2. View\n3. Search\n4. Delete\n5. Exit\nChoose: ")

    if choice == "1":
        contacts.append((input("Name: "), input("Phone: "), input("Email: ")))
        print("Contact added!")

    elif choice == "2":
        for c in contacts:
            print(f"{c[0]}, {c[1]}, {c[2]}")

    elif choice == "3":
        name = input("Enter name: ")
        print(next((f"{c[0]}, {c[1]}, {c[2]}" for c in contacts if c[0].lower() == name.lower()), "Not found"))

    elif choice == "4":
        name = input("Enter name: ")
        contacts = [c for c in contacts if c[0].lower() != name.lower()]
        print("Contact deleted!")

    elif choice == "5":
        break

    else:
        print("Invalid choice!")
