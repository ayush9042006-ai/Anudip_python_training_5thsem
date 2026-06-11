'''Problem 4: School Report Card Generator 
Problem Statement 
Student marks are stored in marks.txt. 
Sample Input/Data (marks.txt) 
S101,Anuj,92 
S102,Rahul,76 
S103,Priya,88 
S104,Neha,45 
S105,Amit,58 
S106,Sneha,95 
S107,Karan,81 
S108,Pooja,73 
S109,Rohit,39 
S110,Anjali,90 
Tasks 1. Calculate grades for all students.  Passed Students: 9 Failed Students: 1 
2. Generate a report card file report_card.txt.  
3. Display topper details.  
4. Count pass and fail students.  
5. Display students eligible for merit certificates (marks ≥ 90).  
'''
# School Report Card Generator

file = open("marks.txt", "r")

report = []
pass_count = 0
fail_count = 0

topper_name = ""
topper_marks = 0
topper_id = ""

merit_students = []

print("STUDENT REPORT")

for line in file:
    sid, name, marks = line.strip().split(",")
    marks = int(marks)

    # Grade Calculation
    if marks >= 90:
        grade = "A+"
    elif marks >= 75:
        grade = "A"
    elif marks >= 60:
        grade = "B"
    elif marks >= 40:
        grade = "C"
    else:
        grade = "F"

    # Pass/Fail Count
    if marks >= 40:
        pass_count += 1
    else:
        fail_count += 1

    # Topper
    if marks > topper_marks:
        topper_marks = marks
        topper_name = name
        topper_id = sid

    # Merit Certificate
    if marks >= 90:
        merit_students.append(name)

    report.append(f"{sid},{name},{marks},{grade}")

    print(sid, name, marks, grade)

file.close()

# Generate Report Card File
outfile = open("report_card.txt", "w")

for record in report:
    outfile.write(record + "\n")

outfile.close()

# Topper Details
print("\nTOPPER DETAILS")
print("Student ID :", topper_id)
print("Name :", topper_name)
print("Marks :", topper_marks)

# Pass/Fail Count
print("\nRESULT SUMMARY")
print("Passed Students :", pass_count)
print("Failed Students :", fail_count)

# Merit Certificate Students
print("\nMERIT CERTIFICATE STUDENTS")
for student in merit_students:
    print(student)

print("\nReport card generated successfully.")