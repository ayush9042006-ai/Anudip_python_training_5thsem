seat=[1,0,1,1,0,0,1,1,1,0]
count_book=0
count_A=0
avialable=[]
'''.............................................................'''
#count the booked seat and avialable seat
for i in seat:
    if i==1:
        count_book+=1
    else:
         count_A+=1
#display the result.........................
print(f"BOOKED SEAT......{count_book}")
print(f"avialable seat......{count_A}")


# Find first available seat..........................................
for i in range(len(seat)):
    if seat[i] == 0:
        print(f"First available seat = {i+1}")
        break
# Find all available seat numbers......................................
for i in range(len(seat)):
    if seat[i] == 0:
        avialable.append(i+1)

print(f"Available seat numbers{avialable}:")

