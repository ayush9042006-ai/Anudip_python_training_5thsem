seat=[1,0,1,1,0,0,1,1,1,0]
count_book=0
count_A=0
'''.............................................................'''
for i in seat:
    if i==1:
        count_book+=1
    else:
        count_A+=1



print(f"BOOKED SEAT......{count_book}")
print(f"avialable seat......{count_A}")

