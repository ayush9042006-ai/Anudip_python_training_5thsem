'''prices = { 
    "Laptop": 55000, 
    "Mouse": 800, 
    "Keyboard": 1800, 
    "Monitor": 12000, 
    "Printer": 9000, 
    "Tablet": 28000, 
    "Speaker": 3500, 
    "Webcam": 2500, 
    "Headphones": 4200, 
    "Router": 3200 
} 
Tasks 
• Display products costing more than ₹5000.  
• Count products costing less than ₹3000.  
• Find the most expensive product.  
• Create a list of products priced between ₹2000 and ₹10000.  
• Calculate the total value of all products.  '''

prices = {
    "Laptop": 55000,
    "Mouse": 800,
    "Keyboard": 1800,
    "Monitor": 12000,
    "Printer": 9000,
    "Tablet": 28000,
    "Speaker": 3500,
    "Webcam": 2500,
    "Headphones": 4200,
    "Router": 3200
}

# Products costing more than 5000
print("Products costing more than 5000:")
for product in prices:
    if prices[product] > 5000:
        print(product)

# Count products costing less than 3000
count = 0
for product in prices:
    if prices[product] < 3000:
        count += 1

print("Products costing less than 3000 =", count)

# Most expensive product
max_price = 0
max_product = ""

for product in prices:
    if prices[product] > max_price:
        max_price = prices[product]
        max_product = product

print("Most expensive product =", max_product)
print("Price =", max_price)

# Products priced between 2000 and 10000
lst = []

for product in prices:
    if prices[product] >= 2000 and prices[product] <= 10000:
        lst.append(product)

print("Products priced between 2000 and 10000:")
print(lst)

# Total value of all products
total = 0

for product in prices:
    total += prices[product]

print("Total value of all products =", total)