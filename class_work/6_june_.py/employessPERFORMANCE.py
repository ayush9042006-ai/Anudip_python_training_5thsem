employ=(
    ("E101","anuj",92),
    ("E102","rahul",76),
    ("E103","priya",58),
    ("E104","neha",88),
    ("E105","amit",45)

)

count=0
print("employess score 80 or above.....")
for i in employ:
    if i[2] >=80:
        print(i[0],i[1],i[2])
#...........................................
for i in employ:
    if i[2] < 60:
        count+=1
print("Employees Needing Improvement:",count)


# highest score ....................
high=employ[0]
for i in employ:
    if i[2] > high[2]:
        high= i
print("highest performance",high)

high_performers = []
#list which store score more than 75
for emp in employ:
    if emp[2] > 75:
        high_performers.append(emp[1])

print("High Performers:", high_performers)



# display performance of employess
print("Performance Categories:")

for emp in employ:
    name = emp[1]
    score = emp[2]

    if score >= 90:
        category = "Excellent"
    elif score >= 75:
        category = "Good"
    elif score >= 60:
        category = "Average"
    else:
        category = "Needs Improvement"

    print(name, ".....>", category)