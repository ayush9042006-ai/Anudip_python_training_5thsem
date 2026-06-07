'''contacts = { 
    "Amit": "9876543210", 
    "Priya": "9876543211", 
    "Rohan": "9876543212", 
    "Neha": "9876543213", 
    "Anjali": "9876543214", 
    "Karan": "9876543215", 
    "Pooja": "9876543216", 
    "Arjun": "9876543217", 
    "Sneha": "9876543218", 
    "Rahul": "9876543219" 
} 
Tasks 
• Display all contact names in alphabetical order.  
• Count the total number of contacts.  
• Search for a given contact name.  
• Create a list of contacts whose names start with a vowel.  
• Stop the search using break once the required contact is found.  '''

contacts = {
    "Amit": "9876543210",
    "Priya": "9876543211",
    "Rohan": "9876543212",
    "Neha": "9876543213",
    "Anjali": "9876543214",
    "Karan": "9876543215",
    "Pooja": "9876543216",
    "Arjun": "9876543217",
    "Sneha": "9876543218",
    "Rahul": "9876543219"
}

# 1. Display all contact names in alphabetical order
print("Contacts in alphabetical order:")
for name in sorted(contacts):
    print(name)

# 2. Count total contacts
print("Total contacts =", len(contacts))

# 3. Search for a given contact name
search = input("Enter contact name to search: ")

found = False
for name in contacts:
    if name == search:
        print(name, "found with number:", contacts[name])
        found = True
        break   # stop search once found

if not found:
    print("Contact not found")

# 4. Contacts whose names start with a vowel
vowels = ['A', 'E', 'I', 'O', 'U']
vowel_list = []

for name in contacts:
    if name[0].upper() in vowels:
        vowel_list.append(name)

print("Contacts starting with vowel:")
print(vowel_list)