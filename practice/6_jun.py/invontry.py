'''2. Inventory Management System 
Sample Data 
inventory = { 
    "Notebook": 45, 
    "Pen": 120, 
    "Pencil": 80, 
    "Eraser": 25, 
    "Marker": 15, 
    "Stapler": 8, 
    "Glue": 12, 
    "Scale": 30, 
    "Folder": 5, 
    "Calculator": 3 
} 
Tasks 
• Display products with stock less than 10.  
• Count products having stock more than 50.  
• Find the product with the minimum stock.  
• Create a list of products that require restocking (stock < 20).  
• Calculate the total inventory count. '''

inventory = {
    "Notebook": 45,
    "Pen": 120,
    "Pencil": 80,
    "Eraser": 25,
    "Marker": 15,
    "Stapler": 8,
    "Glue": 12,
    "Scale": 30,
    "Folder": 5,
    "Calculator": 3
}

# Products with stock less than 10
print("Products with stock less than 10:")
for product in inventory:
    if inventory[product] < 10:
        print(product)

# Count products having stock more than 50
count = 0
for product in inventory:
    if inventory[product] > 50:
        count += 1

print("Products with stock more than 50 =", count)

# Product with minimum stock
min_stock = list(inventory.values())[0]
min_product = list(inventory.keys())[0]

for product in inventory:
    if inventory[product] < min_stock:
        min_stock = inventory[product]
        min_product = product

print("Product with minimum stock =", min_product)
print("Stock =", min_stock)

# Products requiring restocking
restock = []

for product in inventory:
    if inventory[product] < 20:
        restock.append(product)

print("Products requiring restocking:")
print(restock)

# Total inventory count
total = 0

for product in inventory:
    total += inventory[product]

print("Total Inventory Count =", total)