'''5. Smart Electricity Billing System 
Problem Statement 
Monthly electricity consumption (units) is stored as: 
units = {     "House101": 320,     
            "House102": 180,     
            "House103": 510,     
            "House104": 275,     
            "House105": 150,     
            "House106": 430,     
            "House107": 220,     
            "House108": 390,     
            "House109": 145,     
            "House110": 600 } 
Tasks 1. Display houses consuming more than 400 units.  
2. Find the highest-consuming house.  
3. Find the lowest-consuming house.  
4. Calculate total units consumed.  
5. Create lists:  o Low Consumption (< 200)  o Medium Consumption (200–400)  o High Consumption (> 400)  
6. Count houses eligible for an energy-saving campaign (consumption > 300). ''' 



units = {
    "House101": 320,
    "House102": 180,
    "House103": 510,
    "House104": 275,
    "House105": 150,
    "House106": 430,
    "House107": 220,
    "House108": 390,
    "House109": 145,
    "House110": 600
}

# 1. Houses consuming more than 400 units....................................................
print("Houses consuming more than 400 units:")
for i in units:
    if units[i] > 400:
        print(i, ":", units[i])

# 2. Highest-consuming house.........................................................
high = max(units, key=units.get)
print("Highest-consuming house:")
print(high, ":", units[high])

# 3. Lowest-consuming house.......................................................
low = min(units, key=units.get)
print("Lowest-consuming house:")
print(low, ":", units[low])

# 4. Total units consumed..................................................................
total = sum(units.values())
print("Total units consumed:", total)

# 5. Create lists
low = []
medium= []
high = []

for house in units:
    if units[house] < 200:
        low.append(house)
    elif units[house] <= 400:
        medium.append(house)
    else:
        high.append(house)

print("Low Consumption:", low)
print("Medium Consumption:", medium)
print("High Consumption:", high)

# 6. Count houses with consumption > 300
count = 0

for i in units:
    if units[i] > 300:
        count += 1

print("Houses eligible for energy-saving campaign:", count)