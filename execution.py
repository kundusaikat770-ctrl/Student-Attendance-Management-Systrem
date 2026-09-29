#STUDENT ATTENDANCE MANAGEMENT SYSTEM
# Terminal colors
BLUE = "\033[94m"
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"
students = []

def color_status(status):
    if status == "P":
        return GREEN + status + RESET
    if status == "A":
        return RED + status + RESET
    return status

# MODULE 1: STUDENT MANAGEMENT
def add_students():

    print("\n======================================")
    print(BLUE + "        ADD STUDENTS" + RESET)
    print("======================================")

    try:
        number = int(input("How many students do you want to add? "))

        if number <= 0:
            print("Please enter a valid number.")
            return

        for i in range(number):

            print("\nStudent", i + 1)

            roll = int(input("Enter Roll Number: "))

            # Check duplicate roll number
            duplicate = False

            for student in students:
                if student[0] == roll:
                    duplicate = True
                    break

            if duplicate:
                print("This Roll Number already exists.")
                continue

            name = input("Enter Student Name: ")

            if name.strip() == "":
                print("Name cannot be empty.")
                continue

            students.append([roll, name, 0, 0])

            print("Student added successfully.")

    except ValueError:
        print("Invalid input! Please enter a number.")
def view_students():

    print("\n======================================")
    print(BLUE + "          STUDENT LIST" + RESET)
    print("======================================")

    if len(students) == 0:
        print("No students have been added.")
        return

    print("-" * 65)

    print(
        "Roll No".ljust(10),
        "Name".ljust(25),
        "Total".ljust(10),
        "Present".ljust(10)
    )

    
    print("-" * 65)
def search_student():

    print("\n======================================")
    print(BLUE + "          SEARCH STUDENT" + RESET)
    print("======================================")

    try:
        roll = int(input("Enter Roll Number: "))

        for student in students:

            if student[0] == roll:

                print("\nStudent Found!")
                print("-----------------------------")
                print("Roll Number :", student[0])
                print("Name        :", student[1])
                print("Total Class :", student[2])
                print("Present     :", student[3])
                print("Absent      :", student[2] - student[3])

                if student[2] > 0:
                    percentage = (
                        student[3] / student[2]
                    ) * 100
                else:
                    percentage = 0

                print(
                    "Attendance  :",
                    round(percentage, 2),
                    "%"
                )

                return

        print("Student not found.")

    except ValueError:
        print("Invalid Roll Number.")

# MODULE 2: ATTENDANCE MANAGEMENT
def take_attendance():
    print("\n======================================")
    print(BLUE + "          TAKE ATTENDANCE" + RESET)
    print("======================================")

    if len(students) == 0:
        print("No students available.")
        return

    print("\nEnter " + GREEN + "P" + RESET + " for Present")
    print("Enter " + RED + "A" + RESET + " for Absent")

    print()

    for student in students:

        while True:

            status = input(
                str(student[0]) + " - " +
                student[1] +
                " : "
            ).upper()
            if status == "P":
                print(GREEN + "P" + RESET)
            elif status == "A":
                print(RED + "A" + RESET)

            if status == "P":

                student[2] += 1
                student[3] += 1

                break

            elif status == "A":

                student[2] += 1

                break

            else:

                print(
                    "Invalid input! "
                    "Please enter P or A."
                )

    print("\nAttendance recorded successfully!")
def mark_individual_attendance():
    print("\n======================================")
    print(BLUE + "     INDIVIDUAL ATTENDANCE" + RESET )
    print("======================================")

    try:
        roll = int(input("Enter Roll Number: "))
        
        # Search for the student
        for student in students:
            if student[0] == roll:
                # Keep asking for input until a valid choice ('P' or 'A') is given
                while True:
                    status = input("Enter P for Present or A for Absent: ").upper()
                    
                    if status == "P":
                        student[2] += 1  # Total classes
                        student[3] += 1  # Attended classes
                        print("Student marked Present.")
                        return
                    elif status == "A":
                        student[2] += 1  # Total classes
                        print("Student marked Absent.")
                        return
                    else:
                        print("Invalid input. Please enter P or A.")
        
        # This executes if the loop finishes without finding the roll number
        print("Student not found.")

    except ValueError:
        print("Invalid Roll Number.")

# MODULE 3: REPORTS AND ANALYTICS
def attendance_report():
    print("\n======================================")
    print(BLUE + "        ATTENDANCE REPORT" + RESET)
    print("======================================")
    if len(students) == 0:
        print("No students available.")
        return
    print("-" * 85)
    print(
        "Roll".ljust(8),
        "Name".ljust(25),
        "Total".ljust(10),
        "Present".ljust(10),
        "Absent".ljust(10),
        "Percentage"
    )
    print("-" * 85)
    for student in students:
        roll = student[0]
        name = student[1]
        total = student[2]
        present = student[3]
        absent = total - present
        if total > 0:
            percentage = (
                present / total
            ) * 100
        else:
            percentage = 0
        print(
            str(roll).ljust(8),
            name.ljust(25),
            str(total).ljust(10),
            str(present).ljust(10),
            str(absent).ljust(10),
            str(round(percentage, 2)) + "%"
        )
    print("-" * 85)
def low_attendance():

    print("\n======================================")
    print(BLUE + "    LOW ATTENDANCE STUDENTS    " + RESET)
    print("======================================")
    found = False
    for student in students:
        if student[2] > 0:
            percentage = (
                student[3] / student[2]
            ) * 100
            if percentage < 75:
                found = True
            print(
                    "Roll No:",
                    student[0],
                    "| Name:",
                    student[1],
                    "| Attendance:",
                    round(percentage, 2),
                    "%"
                )
    if found == False:
      print(
            "No student has attendance below 75%."
        )

def class_summary():

    print("\n======================================")
    print( BLUE + "          CLASS SUMMARY" + RESET)
    print("======================================")

    if len(students) == 0:
        print("No students available.")
        return
    total_students = len(students)
    total_classes = 0
    total_present = 0
    for student in students:
        total_classes += student[2]
        total_present += student[3]

    print("Total Students :", total_students)
    print("Total Classes  :", total_classes)
    print("Total Present  :", total_present)

    if total_classes > 0:

        overall_percentage = (
            total_present / total_classes
        ) * 100

    else:

        overall_percentage = 0

    print(
        "Overall Attendance :",
        round(overall_percentage, 2),
        "%"
    )

# MAIN MENU

def main():

    print("\n")
    print("===================================================")
    print("      STUDENT ATTENDANCE MANAGEMENT SYSTEM")
    print("===================================================")
    print("              VITyarthi Project")
    print("===================================================")

    while True:

        print("\n")
        print("--------------- MAIN MENU ----------------")
        print("1. Add Students")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Take Attendance")
        print("5. Mark Individual Attendance")
        print("6. Attendance Report")
        print("7. Low Attendance Students")
        print("8. Class Summary")
        print("9. Exit")
        print("-------------------------------------------")

        choice = input(
            "Enter your choice: "
        )
        if choice == "1":
         add_students()
        elif choice == "2":
         view_students()
        elif choice == "3":
         search_student()
        elif choice == "4":
         take_attendance()
        elif choice == "5":
         mark_individual_attendance()
        elif choice == "6":
         attendance_report()
        elif choice == "7":
         low_attendance()
        elif choice == "8":
         class_summary()
        elif choice == "9":
            print("\nThank you for using the system!")
            print("Project completed successfully.")
            break
        else:
            print(
                "\nInvalid choice! "
                "Please select 1 to 9."
            )
main()