'''A software license key is entered: 
ABCD-EFGH-IJKL-MNOP 
Tasks 
Write a program to: 
1. Verify there are exactly 4 groups.  
2. Verify each group contains exactly 4 characters.  
3. Count total letters.  
4. Count vowels.  
5. Remove hyphens and display the merged key.  
6. Create a list containing all groups.  
7. Display whether the key format is valid.  '''
 
key = "ABCD-EFGH-IJKL-MNOP"
 
# 1. Split into groups
groups = key.split("-")
 
# 2. Verify number of groups
group_count = len(groups)
 
# 3. Verify each group length = 4
valid = True
for g in groups:
    if len(g) != 4:
        valid = False
 
# 4. Count letters and vowels
letters = 0
vowels = 0
 
for ch in key:
    if ch.isalpha():
        letters += 1
        if ch in "AEIOUaeiou":
            vowels += 1
 
# 5. Merge key (remove hyphens)
merged = ""
for ch in key:
    if ch != "-":
        merged += ch
 
# 6. Final validation
if group_count == 4 and valid:
    status = "Valid"
else:
    status = "Invalid"
 
# Output
print("License Key:")
print(key)
 
print("\nGroups:")
print(groups)
 
print("\nNumber of Groups:", group_count)
 
print("\nTotal Letters:", letters)
print("Total Vowels:", vowels)
 
print("\nMerged Key:")
print(merged)
 
print("\nLicense Key Status:", status)