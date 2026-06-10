'''8. String-Based Attendance Tracker 
Problem Statement 
Attendance of a student for 15 days is represented as: 
PPAPPPAAPPPPAPP 
Where: • P = Present  
       • A = Absent  
Tasks Write a program to: 
1. Count Present and Absent days.  
2. Calculate attendance percentage.  
3. Find the longest consecutive streak of Presence.  
4. Find the longest consecutive streak of Absence.  
5. Determine whether attendance is below 75%'''



attendance = "PPAPPPAAPPPPAPP"

# Count Present and Absent
p= 0
ab= 0
for i in attendance:
    if i == "P":
        p+= 1
    else:
        ab+= 1
# Attendance Percentage
percentage = (p/ len(attendance)) * 100

# Longest Present Streak
maxp = 0
current_p = 0
for i in attendance:
    if i== "P":
        current_p += 1
        if current_p > maxp:
            maxp = current_p
    else:
        current_p = 0
# Longest Absent Streak
max_ab = 0
current_ab = 0
for i in attendance:
    if i== "A":
        current_ab+= 1
        if current_ab > max_ab:
            max_ab = current_a
    else:
        current_a = 0
# Attendance Status
if percentage < 75:
    status = "Below 75%"
else:
    status = "Above 75%"
# Output
print("Attendance Record :", attendance)
print("Present Days :", p)
print("Absent Days :", ab)
print("Attendance Percentage :", round(percentage, 2),"%")
print("Longest Present Streak :", maxp)
print("Longest Absent Streak :", max_ab)
print("Attendance Status :", status)