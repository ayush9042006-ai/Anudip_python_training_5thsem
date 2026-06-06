slots=[1,0,1,1,0,0,1,0]
count_book=0
count_A=0
avialable=[]
'''.............................................................'''
#count the booked seat and avialable seat
for i in slots:
    if i==1:
        count_book+=1
    else:
         count_A+=1
#display the result.........................
print(f"occupied slots......{count_book}")
print(f"avialable slots......{count_A}")


# Find first available seat..........................................
for i in range(len(slots)):
    if slots[i] == 0:
        print(f"First available slots = {i+1}")
        break
# Find all available seat numbers......................................
for i in range(len(slots)):
    if slots[i] == 0:
        avialable.append(i+1)

print(f"Available slots numbers{avialable}:")
