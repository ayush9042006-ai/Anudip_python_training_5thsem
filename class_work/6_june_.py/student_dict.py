attendance = {}

for i in range(3):
    rollno = input("Enter roll number: ")
    status = input("Enter Attendance (Present/Absent): ")

    attendance[rollno] = status

print("Students who are Present:")

for roll in attendance:
    if attendance[roll] == "Present":
        print(roll)

print("Complete Attendance Record:")
print(attendance)