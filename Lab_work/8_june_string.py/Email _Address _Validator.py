'''6. Email Address Validator 
Problem Statement 
A user enters an email address: 
rahul.sharma2026@gmail.com 
Tasks Write a program to: 
1. Extract username.  
2. Extract domain name.  
3. Extract extension.  
4. Count digits present in username.  
5. Count special characters.  
6. Check whether:  o Exactly one '@' exists.  o At least one '.' exists after '@'.  
7. Display Valid Email or Invalid Email.'''

email = input("Enter Email Address: ")

# 1. Extract username
username = email.split("@")[0]

# 2. Extract domain name
domain = email.split("@")[1].split(".")[0]

# 3. Extract extension
extension = email.split(".")[-1]

# 4. Count digits in username
digit_count = 0
for ch in username:
    if ch.isdigit():
        digit_count += 1

# 5. Count special characters in username
special_count = 0
for ch in username:
    if not ch.isalnum():
        special_count += 1

# 6. Validation
if email.count("@") == 1:
    at_pos = email.index("@")

    if "." in email[at_pos:]:
        valid = True
    else:
        valid = False
else:
    valid = False

# Display Results
print("\nUsername :", username)
print("Domain Name :", domain)
print("Extension :", extension)
print("Digits in Username :", digit_count)
print("Special Characters :", special_count)

if valid:
    print("Valid Email")
else:
    print("Invalid Email")