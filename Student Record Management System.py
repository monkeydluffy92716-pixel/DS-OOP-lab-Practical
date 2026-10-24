class Node:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks
        self.next = None


class StudentRecord:
    def __init__(self):
        self.head = None

    # Add student
    def add(self, roll, name, marks):
        new_node = Node(roll, name, marks)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

        print("Student added successfully.")

    # Display all students
    def display(self):
        if self.head is None:
            print("No student records found.")
            return

        print("\nRoll No\tName\tMarks")
        temp = self.head
        while temp:
            print(temp.roll, "\t", temp.name, "\t", temp.marks)
            temp = temp.next

    # Search student by roll number
    def search(self, roll):
        temp = self.head
        while temp:
            if temp.roll == roll:
                print("Found:", temp.roll, temp.name, temp.marks)
                return
            temp = temp.next
        print("Student not found.")

    # Delete student by roll number
    def delete(self, roll):
        temp = self.head
        prev = None

        while temp:
            if temp.roll == roll:
                if prev is None:
                    self.head = temp.next
                else:
                    prev.next = temp.next
                print("Student deleted successfully.")
                return

            prev = temp
            temp = temp.next

        print("Student not found.")

    # Update student details
    def update(self, roll, name, marks):
        temp = self.head
        while temp:
            if temp.roll == roll:
                temp.name = name
                temp.marks = marks
                print("Student updated successfully.")
                return
            temp = temp.next

        print("Student not found.")

    # Sort records by marks or roll number
    def sort(self, key, order):
        students = []
        temp = self.head

        while temp:
            students.append(temp)
            temp = temp.next

        if key == "marks":
            students.sort(key=lambda s: s.marks, reverse=(order == "desc"))
        else:
            students.sort(key=lambda s: s.roll, reverse=(order == "desc"))

        self.head = None
        for student in students:
            student.next = None
            if self.head is None:
                self.head = student
                tail = student
            else:
                tail.next = student
                tail = student

        print("Records sorted successfully.")
        self.display()


# Main program
system = StudentRecord()

while True:
    print("\n1. Add Student")
    print("2. Delete Student")
    print("3. Update Student")
    print("4. Search Student")
    print("5. Sort Records")
    print("6. Display Records")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        roll = int(input("Enter roll number: "))
        name = input("Enter name: ")
        marks = float(input("Enter marks: "))
        system.add(roll, name, marks)

    elif choice == "2":
        system.delete(int(input("Enter roll number: ")))

    elif choice == "3":
        roll = int(input("Enter roll number to update: "))
        name = input("Enter new name: ")
        marks = float(input("Enter new marks: "))
        system.update(roll, name, marks)

    elif choice == "4":
        system.search(int(input("Enter roll number: ")))

    elif choice == "5":
        key = input("Sort by marks or roll: ").lower()
        order = input("Enter asc or desc: ").lower()

        if key in ("marks", "roll") and order in ("asc", "desc"):
            system.sort(key, order)
        else:
            print("Invalid sorting option.")

    elif choice == "6":
        system.display()

    elif choice == "7":
        print("Exiting program.")
        break

    else:
        print("Invalid choice.")