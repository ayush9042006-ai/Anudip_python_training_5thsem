'''1. Online Shopping Order Analytics Problem Statement An e-commerce company stores product sales data as: 
sales = {"Laptop": 15, 
        "Mouse": 45,
        "Keyboard": 32, 
        "Monitor": 12, 
        "Headphones": 28,
        "Printer": 8,
        "Webcam": 20, 
        "Speaker": 18,
        "Tablet": 10,
        "Router": 25 }
 Tasks 1. Display products sold more than 20 times. 
2. Find the best-selling product. 
3. Find the least-selling product.  
4. Calculate total products sold.
5. Create a list of products requiring promotion (sales < 15)
6. Count products having sales between 10 and 30.  '''


sales = {
               "Laptop": 15,
              "Mouse": 45,
              "Keyboard": 32,
              "Monitor": 12,
             "Headphones": 28,
             "Printer": 8,
            "Webcam": 20,
            "Speaker": 18,
             "Tablet": 10,
            "Router": 25
}

# 1. Display products sold more than 20 times.........................................
print("Products sold more than 20 times...:")
for p, q in sales.items():
    if q > 20:
        print(p, "---->", q)

# 2. Find the best-selling product
bestPRO = max(sales, key=sales.get)
print("Best selling product...............:")
print(bestPRO, ":", sales[bestPRO])

# 3. Find the least-selling product....................................................
least = min(sales, key=sales.get)
print("Least selling product.........:")
print(least, ":", sales[least])

# 4. Calculate total products sold
total= sum(sales.values())
print("Total products sold..........:", total)

# 5. Create a list of products requiring promotion.....................................
list = []
for p, q in sales.items():
    if q < 15:
        list.append(p)
print("Products requiring promotion:")
print(list)

# 6. Count products having sales between 10 and 30....................................
count = 0
for q in sales.values():
    if 10<= q <= 30:
        count += 1

print("Number of products sales between 10 and 30:", count)
