'''Problem 8: Smart Water Consumption Monitoring System 
Problem Statement 
Monthly water consumption (in litres) of households is recorded below. 
Sample Data water_usage = {"House101": 1800,"House102": 2200,    
                   "House103": 3500,     
                   "House104": 2800,     
                   "House105": 1600,     
                   "House106": 4100,     
                   "House107": 2400,     
                   "House108": 3900,     
                   "House109": 1500,     
                   "House110": 4500 } 
Tasks 1. Display houses consuming more than 3000 litres.  
2. Find the highest and lowest consumers.  
3. Calculate total water consumption.  
4. Categorize houses:  o Low (<2000 litres)  o Medium (2000–3500 litres)  o High (>3500 litres)  
5. Count households eligible for conservation awareness programs (>2500 litres).'''



# Smart Water Consumption Monitoring System

water_usage = {
    "House101": 1800,
    "House102": 2200,
    "House103": 3500,
    "House104": 2800,
    "House105": 1600,
    "House106": 4100,
    "House107": 2400,
    "House108": 3900,
    "House109": 1500,
    "House110": 4500
}

# 1. Houses consuming more than 3000 litres
print("Houses Consuming More Than 3000 Litres:")

for house, usage in water_usage.items():
    if usage > 3000:
        print(house, ":", usage, "litres")

# 2. Highest and Lowest Consumers
highest_house = max(water_usage, key=water_usage.get)
lowest_house = min(water_usage, key=water_usage.get)

print("\nHighest Consumer:")
print(highest_house, "-", water_usage[highest_house], "litres")

print("\nLowest Consumer:")
print(lowest_house, "-", water_usage[lowest_house], "litres")

# 3. Total Water Consumption
total = sum(water_usage.values())

print("\nTotal Water Consumption:", total, "litres")

# 4. Categorize Houses
print("\nHouse Categories")

for house, usage in water_usage.items():

    if usage < 2000:
        category = "Low"

    elif usage <= 3500:
        category = "Medium"

    else:
        category = "High"

    print(house, ":", category)

# 5. Conservation Awareness Program (>2500 litres)
count = 0

for usage in water_usage.values():
    if usage > 2500:
        count += 1

print("\nHouseholds Eligible for Conservation Awareness Program:", count)