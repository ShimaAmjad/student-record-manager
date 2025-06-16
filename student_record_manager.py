
# 📚 Student Record Manager

students = []

def show_menu():
    print("\n📋 Student Record Menu")
    print("1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Exit")

def add_student():
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    grade = input("Enter student grade: ")
    student = {"name": name, "age": age, "grade": grade}
    students.append(student)
    print(f"✅ Student {name} added successfully.")

def view_students():
    if not students:
        print("⚠️ No students found.")
    else:
        print("\n👥 Student List:")
        for idx, student in enumerate(students, 1):
            print(f"{idx}. {student['name']}, Age: {student['age']}, Grade: {student['grade']}")

def delete_student():
    name = input("Enter student name to delete: ")
    for student in students:
        if student["name"].lower() == name.lower():
            students.remove(student)
            print(f"🗑 Student {name} deleted successfully.")
            return
    print(f"❌ Student {name} not found.")

# Main loop
while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        delete_student()
    elif choice == "4":
        print("👋 Exiting program. Goodbye!")
        break
    else:
        print("⚠️ Invalid option. Please try again.")
