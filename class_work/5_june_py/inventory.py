stock1=[25,5,0,12,3,18,0,30]
out_stock=0
restock=[]
count=0
healthy=[]


for i in stock1:
    if i==0:
        out_stock+=1
    if i < 10:
        restock.append(i)
    if i> 0:
        count+=1
    if i >=15 :
        healthy.append(i)



            
print("OUT OF STOCK PRODUCTS...",out_stock)
print(f"Restock reqired..{restock}")
print(f"available stock: {count}")
print(f"healthy stock {healthy}")
