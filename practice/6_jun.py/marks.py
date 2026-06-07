'''1. Student Marks Analysis 
Sample Data 
marks = { 
    "Aarav": 78, 
    "Diya": 92, 
    "Rohan": 45, 
    "Ishita": 88, 
    "Kabir": 56, 
    "Meera": 39, 
    "Arjun": 95, 
    "Saanvi": 67, 
    "Vivaan": 82, 
    "Anaya": 51 
} 
Tasks 
• Display students scoring 80 or above.  
• Count the number of students who failed (marks < 40).  
• Find the highest scorer.  
• Create a list of students scoring between 60 and 75.  
• Assign grades:  
o A: ≥ 90  
o B: 75–89  
o C: 50–74  
o F: < 50  '''

marks = {
    "Aarav": 78,
    "Diya": 92,
    "Rohan": 45,
    "Ishita": 88,
    "Kabir": 56,
    "Meera": 39,
    "Arjun": 95,
    "Saanvi": 67,
    "Vivaan": 82,
    "Anaya": 51
}

# Students scoring 80 or above
print("Students scoring 80 or above:")
for name in marks:
    if marks[name] >= 80:
        print(name)

# Count failed students
failed = 0
for name in marks:
    if marks[name] < 40:
        failed += 1

print("Failed Students =", failed)

# Highest scorer
highest_marks = 0
highest_student = ""

for name in marks:
    if marks[name] > highest_marks:
        highest_marks = marks[name]
        highest_student = name

print("Highest Scorer =", highest_student)
print("Marks =", highest_marks)

# Students scoring between 60 and 75
lst = []

for name in marks:
    if marks[name] >= 60 and marks[name] <= 75:
        lst.append(name)

print("Students scoring between 60 and 75:")
print(lst)

# Assign Grades
print("Grades:")

for name in marks:
    if marks[name] >= 90:
        grade = "A"
    elif marks[name] >= 75:
        grade = "B"
    elif marks[name] >= 50:
        grade = "C"
    else:
        grade = "F"

    print(name, ":", grade)