







def display_all():
    file = open("student.txt", "r")
    print("Employee Records")
    print("-" * 40)
    for line in file:
        empid, name, salary = line.strip().split(",")
        print("ID:", empid, "Name:", name, "Salary:", salary)

    file.close()


def search_employee():
    search_id = input("Enter Employee ID: ")

    file = open("student.txt", "r")
    found = False

    for line in file:
        empid, name, salary = line.strip().split(",")

        if empid == search_id:
            print("\nEmployee Found")
            print("ID:", empid)
            print("Name:", name)
            print("Salary:", salary)
            found = True
            break

    if not found:
        print("Employee Not Found")

    file.close()


def average_salary():
    file = open("student.txt", "r")

    total = 0
    count = 0

    for line in file:
        empid, name, salary = line.strip().split(",")
        total += int(salary)
        count += 1

    avg = total / count
    print("Average Salary =", round(avg, 2))

    file.close()


def highest_lowest_salary():
    file = open("student.txt", "r")

    employees = []

    for line in file:
        empid, name, salary = line.strip().split(",")
        employees.append((empid, name, int(salary)))

    highest = employees[0]
    lowest = employees[0]

    for emp in employees:
        if emp[2] > highest[2]:
            highest = emp

        if emp[2] < lowest[2]:
            lowest = emp

    print("\nHighest Paid Employee")
    print(highest)

    print("\nLowest Paid Employee")
    print(lowest)

    file.close()


def salary_above_50000():
    file = open("student.txt", "r")

    print("\nEmployees Earning Above ₹50,000")

    for line in file:
        empid, name, salary = line.strip().split(",")

        if int(salary) > 50000:
            print(empid, name, salary)

    file.close()


def add_employee():
    empid = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    salary = input("Enter Salary: ")

    file = open("student.txt", "a")
    file.write("\n" + empid + "," + name + "," + salary)
    file.close()

    print("Employee Record Added Successfully")


def salary_category():
    file = open("student.txt", "r")

    print("\nSalary Categories")
    print("-" * 40)

    for line in file:
        empid, name, salary = line.strip().split(",")
        salary = int(salary)

        if salary >= 60000:
            category = "High"

        elif salary >= 40000:
            category = "Medium"

        else:
            category = "Low"

        print(empid, name, salary, "->", category)

    file.close()


while True:
    print("\n===== Employee Payroll Management =====")
    print("1. Display All Employees")
    print("2. Search Employee")
    print("3. Average Salary")
    print("4. Highest and Lowest Paid Employee")
    print("5. Employees Earning Above ₹50,000")
    print("6. Add New Employee")
    print("7. Salary Categories")
    print("8. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        display_all()

    elif choice == 2:
        search_employee()

    elif choice == 3:
        average_salary()

    elif choice == 4:
        highest_lowest_salary()

    elif choice == 5:
        salary_above_50000()

    elif choice == 6:
        add_employee()

    elif choice == 7:
        salary_category()

    elif choice == 8:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")