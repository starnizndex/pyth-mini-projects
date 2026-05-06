# Student Score Tracker

students = []  


def student():
    name = input("Enter student name: ")
    scores = []

    for i in range(3):  
        score = float(input(f"Enter score {i+1}: "))
        scores.append(score)

    student = {
        "name": name,
        "scores": scores
    }

    students.append(student)
    print("Student added successfully!\n")

# Function to display all students
def displayStudents():
    if not students:
        print("No students found.\n")
        return

    for student in students:
        avg = sum(student["scores"]) / len(student["scores"])
        print(f"Name: {student['name']}")
        print(f"Scores: {student['scores']}")
        print(f"Average: {avg:.2f}")
        print("-" * 20)

# Function to search for a student
def searchStudent():
    searchName = input("Enter student name to search: ").lower()

    for student in students:
        if student["name"].lower() == searchName:
            avg = sum(student["scores"]) / len(student["scores"])
            print(f"\nFound: {student['name']}")
            print(f"Scores: {student['scores']}")
            print(f"Average: {avg:.2f}\n")
            return

    print("Student not found.\n")

# Main menu
while True:
    print("=== Student Score Tracker ===")
    print("1. AddStudent")
    print("2. ViewAllStudents")
    print("3. SearchStudent")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        addStudent()
    elif choice == "2":
        displayStudents()
    elif choice == "3":
        searchStudent()
    elif choice == "4":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Try again.\n")