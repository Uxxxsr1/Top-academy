students = []


def show():
    if students:
        for student in students:
            print(f"Name: {student['name']}")
            print(f"Age: {student['yearOlds']}")
            print(f"Address: {student['address']}")
            print(f"Phone: {student['numberOfPhone']}")
            print(f"Course: {student['course']}")
            print("---")
    else:
        print("No students available")


while True:
    hellotext = """Hello! pleas choose :
1. Show information by student
2. Creat new student
3. Update info by student
4. Delete student
5. Exit
Writie only number!"""
    print(hellotext)
    usrinp = int(input(": "))

    if usrinp == 1:
        show()
    elif usrinp == 2:
        nameusr = input("Enter name of new student: ")
        yearusr = int(input("Enter how old the student is: "))
        addressusr = input("Enter address of new student: ")
        numberusr = input("Enter number phone of new user: ")
        coursusr = int(input("Enter course of new student: "))

        student = {
            "name": nameusr,
            "yearOlds": yearusr,
            "address": addressusr,
            "numberOfPhone": numberusr,
            "course": coursusr
        }
        students.append(student)
        print("Student was successfully created!")

    elif usrinp == 3:
        if students:
            show()
            index = int(input("Enter student number to update: ")) - 1
            if 0 <= index < len(students):
                field = input("Enter field to update (name/yearOlds/address/numberOfPhone/course): ")
                if field in students[index]:
                    new_value = input(f"Enter new {field}: ")
                    if field in ["yearOlds", "course"]:
                        new_value = int(new_value)
                    students[index][field] = new_value
                    print("Info was successfully updated!")
                else:
                    print("Invalid field")
            else:
                print("Invalid student number")
        else:
            print("No students to update")

    elif usrinp == 4:
        if students:
            show()
            index = int(input("Enter student number to delete: ")) - 1
            if 0 <= index < len(students):
                deleted = students.pop(index)
                print(f"Student {deleted['name']} was deleted!")
            else:
                print("Invalid student number")
        else:
            print("No students to delete")

    elif usrinp == 5:
        print("Goodbye!")
        break

    else:
        print("Invalid choice")