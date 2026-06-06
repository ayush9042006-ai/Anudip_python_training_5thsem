employees = [
        ("Rahul", 35000),
("Priya", 55000),
    ("Amit", 42000),
    ("Neha", 65000)
]

# Employees earning above 50000......>>>>>>>>>>
print("Employees earning above ..₹50,000:")
for i in employees:
    if i[1] > 50000:
        print(i[0], "-", i[1])
# Find highest-paid employee.........>>>>>>>>>>
high = employees[0]
for i in employees:
    if i[1] > high[1]:
        high = i

print("highest paid employ....:")
print(high[0], "-", high[1])      

# Calculate total salary...........>>>>>>>
total = 0
for i in employees:
    total += i[1]
print("total salary.....:", total)

# Count employees earning below 40000......>>>>>>>>>>>
count = 0
for i in employees:
    if i[1] < 40000:
        count += 1  
print("Employees earning below..>> ₹40000:", count)