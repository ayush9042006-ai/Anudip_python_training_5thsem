''' 1. Employee ID Validation and Analysis System
 Problem Statement 
 A company generates employee IDs in the following format
 : EMP2026ANUJ458 
 Tasks Write a program to:
   1. Count the number of uppercase letters.  
   2. Count the number of digits.  
   3. Extract the joining year. 
     4. Extract the employee name. 
       5. Check whether the ID follows these rules:  o Starts with "EMP"  o Contains exactly 4 digits for the year  o Ends with exactly 3 digits 
         6. Create a list containing all digits present in the ID.
             7. Find the sum of all digits present in the ID.  
             8. Display whether the ID is valid or invalid. '''





emp_id = input("Enter Employee ID: ")

# 1. Count uppercase letters
upper_count = 0

# 2. Count digits
digit_count = 0

# List to store digits
digit_list = []

for ch in emp_id:
    if ch.isupper():
        upper_count += 1

    if ch.isdigit():
        digit_count += 1
        digit_list.append(int(ch))

# 3. Extract joining year
year = emp_id[3:7]

# 4. Extract employee name
name = emp_id[7:-3]

# 5. Validation
valid = True

# Rule 1: Starts with EMP
if not emp_id.startswith("EMP"):
    valid = False

# Rule 2: Year must contain exactly 4 digits
if len(year) != 4 or not year.isdigit():
    valid = False

# Rule 3: Ends with exactly 3 digits
if len(emp_id) < 10 or not emp_id[-3:].isdigit():
    valid = False

# 6. List of all digits
# Already stored in digit_list

# 7. Sum of all digits
digit_sum = sum(digit_list)

# 8. Display Results
print("\n----- Employee ID Analysis -----")
print("Employee ID :", emp_id)
print("Uppercase Letters :", upper_count)
print("Total Digits :", digit_count)
print("Joining Year :", year)
print("Employee Name :", name)
print("Digits List :", digit_list)
print("Sum of Digits :", digit_sum)

if valid:
    print("Status : VALID Employee ID")
else:
    print("Status : INVALID Employee ID")