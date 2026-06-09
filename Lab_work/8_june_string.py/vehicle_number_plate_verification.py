'''  4. Vehicle Number Plate Verification
 Problem Statement 
 A vehicle number plate is entered: MH12AB4589 Tasks Write a program to: 
 1. Extract state code.
 2. Extract district code. 
 3. Extract vehicle series. 
 4. Extract vehicle number.  
 5. Count letters and digits separately.  
 6. Verify:  o First 2 characters must be alphabets.  o Next 2 must be digits.  o Next 2 must be alphabets.  o Last 4 must be digits. 
 7. Display whether the number plate is valid.  '''

plate = 'MH12AB4589'

state = plate[:2]
district = plate[2:4]
series = plate[4:6]
number = plate[6:]

letters = 0
digits = 0

for i in plate:
    if i.isalpha():
        letters += 1
    if i.isdigit():
        digits += 1

print("State Code :", state)
print("District Code :", district)
print("Vehicle Series :", series)
print("Vehicle Number :", number)
print("Letters :", letters)
print("Digits :", digits)

if state.isalpha() and district.isdigit() and series.isalpha() and number.isdigit():
    print("Valid Number Plate")
else:
    print("Invalid Number Plate")