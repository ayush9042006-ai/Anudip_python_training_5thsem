'''7. Username Generator System 
Problem Statement 
A student enters: 
Rahul Sharma 
Tasks Generate a username using the rules: 
1. Remove spaces.  
2. Convert to lowercase.  
3. Append current year (2026).  
4. If username length exceeds 12, keep only first 12 characters.  
5. Count vowels in the generated username.  
6. Count consonants.  
7. Display username statistics'''



name = "Rahul sharma"

# 1. Remove spaces/................................................
username = name.replace(" ", "")
# 2. Convert to lowercase/........................................
username = username.lower()
# 3. Append current year/........................................
username = username + "2026"
# 4. Keep only first 12 characters if length exceeds 12
if len(username) > 12:
    username = username[:12]
print(username)
# 5 & 6. Count vowels and consonants
vowels = 0
consonants = 0

for i in username:
    if i.isalpha():
        if i in "aeiouAEIOU":
            vowels+= 1
        else:
            consonants+= 1

# 7. Display statistics
print("----- Username Statistics -----")
print("Generated Username :", username)
print("Username Length :", len(username))
print("Vowels :", vowels)
print("Consonants :", consonants)