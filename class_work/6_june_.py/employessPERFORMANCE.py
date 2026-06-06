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
