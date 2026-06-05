no=[4,5,6,10,11,15,16,17]
list1=[]
for i in range (len(no)-1):
    if (no[i]+1)==no[i+1]:
        print(f"{no[i]} and {no[i+1]} are consecutive")
        list1.append((no[i],no[i+1]))


print(list1)
