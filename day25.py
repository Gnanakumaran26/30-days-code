print("📊 Student Report Card System - Day 25")

students = []

while True:
    print("\n1. Add Student Report")
    print("2. View All Reports")
    print("3. Quit")

    choice = input("Choose an option (1-3): ")

    if choice == "1":
        name = input("Enter student name: ")
        subjects = ["Math", "Science", "English", "Computer", "History"]
        marks = {}

        total = 0
        for sub in subjects:
            mark = int(input(f"Enter marks for {sub}: "))
            marks[sub] = mark
            total += mark

        average = total / len(subjects)

        if average >= 90:
            grade = "A+"
        elif average >= 75:
            grade = "A"
        elif average >= 60:
            grade = "B"
        elif average >= 45:
            grade = "C"
        else:
            grade = "F"

        student = {
            "name": name,
            "marks": marks,
            "total": total,
            "average": average,
            "grade": grade
        }
        students.append(student)
        print("✅ Report card added!")

    elif choice == "2":
        if not students:
            print("📭 No student reports found.")
        else:
            for stu in students:
                print("\n=============================")
                print(f"🎓 Name: {stu['name']}")
                for sub, mark in stu["marks"].items():
                    print(f"   {sub}: {mark}")
                print(f"   Total: {stu['total']}")
                print(f"   Average: {stu['average']:.2f}")
                print(f"   Grade: {stu['grade']}")
                print("=============================")

    elif choice == "3":
        print("👋 Exiting Report Card System...")
        break

    else:
        print("❌ Invalid option, try again.")
