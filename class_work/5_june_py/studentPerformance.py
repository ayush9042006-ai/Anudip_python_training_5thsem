marks=[78,45,92,35,88,40,99,56]
list1=[]
failCount=0
meritLIST=[]
for i in marks:
    if i > 75:
        meritLIST.append(i) 
    if i >= 40:
        list1.append(i)
    elif i <40:
        failCount+=1
        max_marks=marks[1]
marks.sort()
min_marks=marks[0]
max_marks=marks[len(marks)-1]
print("Passed studentd :",list1)
print("Failed count : ",failCount)
print("Highest marks :",max_marks)
print("minmun marks:",min_marks)
print("Merit list :",meritLIST)










