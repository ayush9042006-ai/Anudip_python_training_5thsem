'''Problem 5: Online Shopping Cart Analyzer 
Problem Statement 
The prices of products added to a shopping cart are stored below. 
Sample Data cart = [1500, 899, 450, 2500, 799, 1200, 300, 650, 1800, 999] 
Tasks 1. Calculate the total cart value.  
2. Find the most expensive and cheapest products.  
3. Count products eligible for premium shipping (price > ₹1000).  
4. Generate a discount list (products above ₹1500).  
5. Calculate the average product price.'''

# Online Shopping Cart Analyzer
cart = [1500, 899, 450, 2500, 799, 1200, 300, 650, 1800, 999]
# 1. Calculate Total Cart Value
total = sum(cart)

print("Total Cart Value ", total)

# 2. Most Expensive and Cheapest Product
highest = max(cart)
lowest = min(cart)

print("Most Expensive Product : ₹", highest)
print("Cheapest Product : ₹", lowest)

# 3. Premium Shipping Products (price > 1000)
premium_count = 0

for price in cart:
    if price > 1000:
        premium_count += 1

print("Premium Shipping Products :", premium_count)

# 4. Discount List (products above 1500)
discount_products = []

for price in cart:
    if price > 1500:
        discount_products.append(price)

print("Products Eligible for Discount :", discount_products)

# 5. Average Product Price
average = total / len(cart)

print("Average Product Price : ₹", round(average, 2))
