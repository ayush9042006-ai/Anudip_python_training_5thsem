'''units = { 
    "House101": 320, 
    "House102": 180, 
    "House103": 450, 
    "House104": 290, 
    "House105": 150, 
    "House106": 510, 
    "House107": 220, 
    "House108": 390, 
    "House109": 170, 
    "House110": 260 
} 
Tasks 
• Display houses consuming more than 300 units.  
• Count houses consuming less than 200 units.  
• Find the house with the highest consumption.  
• Create a list of houses eligible for an energy-saving awareness campaign (consumption > 400 units).  
• Categorize houses as:  
o Low: < 200 units  
o Medium: 200–350 units  
o High: > 350 units'''

units = {
    "House101": 320,
    "House102": 180,
    "House103": 450,
    "House104": 290,
    "House105": 150,
    "House106": 510,
    "House107": 220,
    "House108": 390,
    "House109": 170,
    "House110": 260
}

# Houses consuming more than 300 units
print("Houses consuming more than 300 units:")
for house in units:
    if units[house] > 300:
        print(house)

# Count houses consuming less than 200 units
count = 0
for house in units:
    if units[house] < 200:
        count += 1

print("Houses consuming less than 200 units =", count)

# House with highest consumption
max_units = 0
max_house = ""

for house in units:
    if units[house] > max_units:
        max_units = units[house]
        max_house = house

print("Highest consumption house =", max_house)
print("Units =", max_units)

# Houses for energy-saving campaign (>400)
campaign = []

for house in units:
    if units[house] > 400:
        campaign.append(house)

print("Energy-saving campaign houses:")
print(campaign)

# Categorization
low = []
medium = []
high = []

for house in units:
    if units[house] < 200:
        low.append(house)
    elif units[house] <= 350:
        medium.append(house)
    else:
        high.append(house)

print("Low consumption:", low)
print("Medium consumption:", medium)
print("High consumption:", high)