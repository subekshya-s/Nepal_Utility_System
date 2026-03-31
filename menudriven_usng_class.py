class Student:
    def __init__(self, student_id, name, age):
        self.student_id = student_id
        self.name = name
        self.age = age

    def display(self):
        print(f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}")


class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self):
        student_id = input("Enter ID: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")

        student = Student(student_id, name, age)
        self.students.append(student)
        print("Student added successfully!")

    def show_students(self):
        if len(self.students) == 0:
            print("No students available")
        else:
            for student in self.students:
                student.display()

    def update_student(self):
        student_id = input("Enter ID to update: ")

        for student in self.students:
            if student.student_id == student_id:
                student.name = input("Enter new name: ")
                student.age = input("Enter new age: ")
                print("Student updated successfully!")
                return

        print("Student not found")

    def delete_student(self):
        student_id = input("Enter ID to delete: ")

        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                print("Student deleted successfully!")
                return

        print("Student not found")


# -------- MENU DRIVEN --------
manager = StudentManager()

while True:
    print("\n===== MENU =====")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        manager.add_student()

    elif choice == "2":
        manager.show_students()

    elif choice == "3":
        manager.update_student()

    elif choice == "4":
        manager.delete_student()

    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice, try again!")
