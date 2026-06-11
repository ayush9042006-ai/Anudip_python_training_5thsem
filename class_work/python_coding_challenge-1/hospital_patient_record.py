'''Problem 2: Hospital Patient Record Management System 
Problem Statement 
A hospital maintains patient details in a file named patients.txt. 
Sample Input/Data (patients.txt) 
P101,Anuj,Normal 
P102,Rahul,Critical 
P103,Priya,Stable 
P104,Neha,Critical 
P105,Amit,Stable 
P106,Sneha,Normal 
P107,Karan,Critical 
P108,Pooja,Stable 
P109,Rohit,Normal 
P110,Anjali,Stable 
Tasks 1. Display all patient records.  
2. Display critical patients.  
3. Count patients under each status.  
4. Search patient details using Patient ID.  
5. Save critical patient records to critical_patients.txt. '''



# Hospital Patient Record Management System

# 1. Display all patient records
print("all patient records")
file = open("patients.txt", "r")
for line in file:
    print(line.strip())

file.close()

# 2. Display critical patients
print("\ncritical patients")
file = open("patients.txt", "r")
critical_list = []

for line in file:
    id, name, status = line.strip().split(",")

    if status == "Critical":
        print(id, name, status)
        critical_list.append(line)

file.close()
# 3. Count patients under each status
normal = 0
stable = 0
critical = 0

file = open("patients.txt", "r")
for line in file:
    pid, name, status = line.strip().split(",")

    if status == "Normal":
        normal += 1
    elif status == "Stable":
        stable += 1
    elif status == "Critical":
        critical += 1

file.close()

print("\nPATIENT COUNT BY STATUS")
print("Normal Patients :", normal)
print("Stable Patients :", stable)
print("Critical Patients :", critical)

# 4. Search patient using Patient ID
search= input("\nEnter Patient ID to Search: ")
found = False
file = open("patients.txt", "r")

for line in file:
    id, name, status = line.strip().split(",")

    if id == search:
        print("\nPatient Found")
        print( id,name,status)
        found = True
        break
file.close()
if found == False:
    print("Patient Not Found")

# 5. Save critical patients to another file
outfile = open("critical_patients.txt", "w")

for record in critical_list:
    outfile.write(record)
outfile.close()
print("\nCritical patient records saved successfully.")