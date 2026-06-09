'''2. Password Strength Analyzer
 Problem Statement 
 A user enters a password.
   Python@2026! 
   Tasks Write a program to determine whether the password is Strong, Medium, or Weak.
     Rules: • Minimum length 8  • Contains at least:  o 1 uppercase letter  o 1 lowercase letter  o 1 digit  o 1 special character  Additionally:
       1. Count uppercase letters.  
       2. Count lowercase letters.  
       3. Count digits.  
       4. Count special characters.  
       5. Display all digits separately.  
       6. Display all special characters separately.'''
#.............................................................................
password = input("Enter Password: ")

u = 0
l = 0
d = 0
sp = 0

d_list = []
sp_list = []

for i in password:
    if i.isupper():
        u+= 1
    elif i.islower():
        l+= 1
    elif i.isdigit():
        d+= 1
        d_list.append(ch)
    else:
        sp += 1
        sp_list.append(ch)

# Password Strength Check
if (len(password) >= 8 and u >= 1 and l >= 1 and d >= 1 and sp>= 1):
    strength ="Strong"
elif len(password) >= 8 and (u >= 1 or l >= 1) and d >= 1:
    strength = "Medium"
else:
    strength = "Weak"
#display...........................................................
print("---- Password Analysis -----")
print("Password Length :", len(password))
print("Uppercase Letters :", u)
print("Lowercase Letters :", l)
print("Digits :", d)
print("Special Characters :", sp)

print("Digits Present :", d_list)
print("Special Characters Present :", sp_list)
print("Password Strength :", strength)