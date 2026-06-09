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




# take input id from user....................................
id = input("Enter Employee ID: ")
# count upper case letters..........................................................
UPcount = 0
#count no. of digit
digit_count = 0
# list contain only digit.........................................................
digit=[]
for i in id:
    if i.isupper():
        UPcount += 1

    if i.isdigit():
        digit_count += 1
        digit.append(int(i))
# joining year......................................
year = id[3:7]
# employees name...............................................
name = id[7:-3]
# Check validity
if id.startswith("EMP") and year.isdigit() and id[-3:].isdigit():
    status = "valid id"
else:
    status = "invalid id"

print("Employee ID :", id)
print("Uppercase Letters :", UPcount)
print("Total Digits :", digit_count)
print("Joining Year :", year)
print("Employee Name :", name)
print("Digits List :", digit)
print("Sum of Digits :", sum(digit))
print("Status :", status)