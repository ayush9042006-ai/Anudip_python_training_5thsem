#3. City Temperature Monitoring System Problem 
# Statement Daily temperatures of different cities are stored as: 
# temperature = { "Delhi": 41,    
#               "Mumbai": 33,    
#               "Chennai": 37,  
#               "Kolkata": 39,    
#               "Bengaluru": 28,   
#               "Pune": 30,    
#              "Jaipur": 42,    
#              "Lucknow": 40,    
#              "Hyderabad": 35,    
#               "Ahmedabad": 43 } 
# Tasks 1. Display cities having temperature above 40°C.  
# 2. Find the hottest city. 
# 3. Find the coolest city.
# 4. Calculate average temperature.  
# 5. Create a list of pleasant cities (temperature < 35°C). 
# 6. Count cities with temperature between 35°C and 40°C.  


temperature = {
    "Delhi": 41,
    "Mumbai": 33,
    "Chennai": 37,
    "Kolkata": 39,
    "Bengaluru": 28,
    "Pune": 30,
    "Jaipur": 42,
    "Lucknow": 40,
    "Hyderabad": 35,
    "Ahmedabad": 43
}

# 1. Cities having temperature above 40°C.................................................................
print("Cities having temperature above 40°C:")
for i in temperature:
    if temperature[i] > 40:
        print(i, ":", temperature[i])

# 2. Hottest city...................................................................................
h = max(temperature, key=temperature.get)
print("Hottest City......:")
print(h, ":", temperature[h])

# 3. Coolest city.................................................................................
c= min(temperature, key=temperature.get)
print("Coolest City.......:")
print(c, ":", temperature[c])

# 4. Average temperature...............................................
total = sum(temperature.values())
avg = total / len(temperature)

print("average temperature.......:", avg)

# 5. Pleasant cities (temperature < 35°C)................................................
pleasant = []

for i in temperature:
    if temperature[i] < 35:
        pleasant.append(i)

print("pleasant Cities:")
print(pleasant)

# 6. Count cities with temperature between 35°C and 40°C
count = 0

for i in temperature:
    if 35 <= temperature[i] <= 40:
        count += 1

print("number of cities with temperature between 35°C and 40°C:", count)