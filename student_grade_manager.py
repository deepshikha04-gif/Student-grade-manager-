students = {}

def add_student():
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks
    print("Student added successfully")

def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    else:
        return "D"

def display_students():
    for name, marks in students.items():
        grade = calculate_grade(marks)
        print(name, "Marks:", marks, "Grade:", grade)

while True:
    print("\n1.Add Student")
    print("2.Show Students")
    print("3.Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        break
    else:
        print("Invalid choice")
