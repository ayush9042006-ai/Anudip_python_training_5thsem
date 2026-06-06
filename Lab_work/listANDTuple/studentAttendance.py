attendance = ['P', 'P', 'A', 'P', 'A', 'P', 'P', 'P', 'A', 'P', 'P', 'A', 'P', 'P', 'P']

p= 0
ab = 0

# Count present and absent days
for s in attendance:
    if s == 'P':
        p += 1
    else:
        ab += 1
print("Present Days.........:", p)
print("Absent Days..........:", ab)

# Calculate attendance percentage
total= len(attendance)
per= (p/total) * 100
print("Attendance Percentage:",per,"%")
# Determine eligibility.......>>>>>>
if per>= 75:
    print("Eligible for Exam.....")
else:
    print("Not Eligible for Exam......")
# Display absent positions
print("Absent on Days....:")

for i in range(len(attendance)):
    if attendance[i] == 'A':
        print(i + 1)