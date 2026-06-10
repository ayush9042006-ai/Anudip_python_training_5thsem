'''2. Food Delivery Performance Tracker 
Problem Statement 
Delivery times (in minutes) for different orders are given below: 
delivery_time = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18] 
Requirements Create the following functions: 
1. fastest_delivery(times) Returns the shortest delivery time. 
2. delayed_orders(times) Returns a list of orders taking more than 45 minutes. 
3. average_delivery_time(times) Returns the average delivery time. 
4. delivery_category(times) Displays order categories: • Fast → ≤ 30 minutes  • Normal → 31–45 minutes  • Delayed → > 45 minutes  '''



delivery_time = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18]

#1: Find the fastest delivery..............................................
def fastest_delivery(times):
    return min(times)

#2: Find delayed orders > 45 minutes......................................
def delayed_orders(times):
    delayed = []
    for i in times:
        if i > 45:
            delayed.append(i)
    return delayed

# Function 3: Calculate average delivery time
def average_delivery_time(times):
    return sum(times) / len(times)

# Function 4: Display delivery categories
def delivery_category(times):
    for i in range(len(times)):
        if times[i] <= 30:
            category = "Fast"
        elif times[i] <= 45:
            category = "Normal"
        else:
            category = "Delayed"
            
        print(f"{times[i]}--> {category}")

print("Fastest Delivery Time :", fastest_delivery(delivery_time), "minutes")
print("Delayed Orders :", delayed_orders(delivery_time))
print("Average Delivery Time :", round(average_delivery_time(delivery_time), 2), "minutes")
delivery_category(delivery_time)