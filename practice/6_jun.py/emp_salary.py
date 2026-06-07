'''salary = { 
    "EMP101": 45000, 
    "EMP102": 62000, 
    "EMP103": 38000, 
    "EMP104": 75000, 
    "EMP105": 54000, 
    "EMP106": 29000, 
    "EMP107": 82000, 
    "EMP108": 48000, 
    "EMP109": 36000, 
    "EMP110": 68000 
} 
Tasks 
• Display employees earning above ₹60,000.  
• Count employees earning below ₹40,000.  
• Find the highest-paid employee.  
• Create a list of employees eligible for a bonus (salary > ₹50,000).  
• Calculate the average salary.  '''

salary = {
    "EMP101": 45000,
    "EMP102": 62000,
    "EMP103": 38000,
    "EMP104": 75000,
    "EMP105": 54000,
    "EMP106": 29000,
    "EMP107": 82000,
    "EMP108": 48000,
    "EMP109": 36000,
    "EMP110": 68000
}

# Employees earning above 60000
print("Employees earning above 60000:")
for emp in salary:
    if salary[emp] > 60000:
        print(emp)

# Count employees earning below 40000
count = 0
for emp in salary:
    if salary[emp] < 40000:
        count += 1

print("Employees earning below 40000 =", count)

# Highest paid employee
highest_salary = 0
highest_emp = ""

for emp in salary:
    if salary[emp] > highest_salary:
        highest_salary = salary[emp]
        highest_emp = emp

print("Highest Paid Employee =", highest_emp)
print("Salary =", highest_salary)

# Employees eligible for bonus
bonus = []

for emp in salary:
    if salary[emp] > 50000:
        bonus.append(emp)

print("Employees eligible for bonus:")
print(bonus)

# Average salary
total = 0

for emp in salary:
    total += salary[emp]

average = total / len(salary)

print("Average Salary =", average)