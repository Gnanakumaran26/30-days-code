print("🔄 Unit Converter - KM <-> Miles")

choice = input("Convert from (1) KM to Miles or (2) Miles to KM? Enter 1 or 2: ")

if choice == "1":
    km = float(input("Enter distance in Kilometers: "))
    miles = km * 0.621371
    print(f"{km} KM = {miles:.2f} Miles")

elif choice == "2":
    miles = float(input("Enter distance in Miles: "))
    km = miles / 0.621371
    print(f"{miles} Miles = {km:.2f} KM")

else:
    print("Invalid choice! Please enter 1 or 2.")
