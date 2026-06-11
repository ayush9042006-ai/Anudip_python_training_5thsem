'''Problem 6: Employee Attendance Monitoring System 
Problem Statement Employee attendance records are stored in attendance.txt. 
Sample Input/Data (attendance.txt) 
EMP101,P 
EMP102,A 
EMP103,P 
EMP104,P 
EMP105,A 
EMP106,P 
EMP107,P 
EMP108,A 
EMP109,P 
EMP110,P 
Tasks 1. Count present and absent employees.  
2. Display absent employee IDs.  
3. Calculate attendance percentage.  
4. Generate an absentee report in absent_report.txt.  
5. Display employees eligible for attendance awards (100% attendance).  '''


# Employee Attendance Monitoring System

file = open("attendance.txt", "r")
present = 0
absent = 0
absent_employees = []

print("ABSENT EMPLOYEE IDs")

for line in file:
    emp_id, status = line.strip().split(",")

    if status == "P":
        present += 1
    else:
        absent += 1
        absent_employees.append(emp_id)
        print(emp_id)

file.close()

# 1. Count Present and Absent Employees
print("\nATTENDANCE SUMMARY")
print("Present Employees :", present)
print("Absent Employees :", absent)

# 2. Attendance Percentage
total_employees = present + absent

attendance_percentage = (present / total_employees) * 100

print("Attendance Percentage :",
      round(attendance_percentage, 2), "%")

# 3. Generate Absentee Report
outfile = open("absent_report.txt", "w")

for emp in absent_employees:
    outfile.write(emp + "\n")

outfile.close()

print("\nAbsentee report generated successfully.")

# 4. Employees Eligible for Attendance Awards
print("\nEMPLOYEES ELIGIBLE FOR ATTENDANCE AWARD")

award_found = False

file = open("attendance.txt", "r")

for line in file:
    emp_id, status = line.strip().split(",")

    if status == "P":
        print(emp_id)
        award_found = True
file.close()

if award_found == False:
    print("No employee eligible.")
