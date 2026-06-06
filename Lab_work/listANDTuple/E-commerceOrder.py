orders = [ ("Laptop", 55000),    
           ("Mouse", 800),    
             ("Keyboard", 1500),    
               ("Monitor", 12000),    
                 ("Pen Drive", 600) ]
#display product cost more than 1000

for i in orders:
    if i[1] > 1000:
        print(i[1])

# find most expensive product
max=orders[0]
for i in orders:
    if i[1] > max[1]:
        max=i
print("most expensive...",max)

# total order value
sum=0
for i in orders:
        sum=sum+i[1]

print("total order value...",sum)

#count product costing below than 1000
count=0
for i in orders:
     if i[1] < 1000:
          count+=1
print("count product below:",count)
