'''Problem 3: Smart Parking Management System 
Problem Statement 
The parking status of vehicles in a mall is maintained as follows. 
Sample Data 
parking_slots = ["Occupied", "Vacant", "Occupied", "Vacant","Occupied", "Occupied", "Vacant", "Occupied","Vacant", "Occupied" ] 
Tasks 1. Display vacant parking slot numbers.  
2. Count occupied and vacant slots.  
3. Allocate the first vacant slot to a new vehicle.  
4. Calculate parking occupancy percentage.  
5. Store updated parking information in parking.txt.'''



parking= ["Occupied", "Vacant", "Occupied", "Vacant",     
                 "Occupied", "Occupied", "Vacant", "Occupied",     
                 "Vacant", "Occupied" ] 
#  Display vacant parking slot numbers.  
print("Vacant Parking Slot Numbers:")
for i in range(len(parking)):
    if parking[i] == "Vacant":
        print(i + 1,end=" ")

#Count occupied and vacant slots. 
count_o=0
count_v=0
for i in parking:
    if i=="Occupied":
        count_o+=1
    else:
        count_v+=1
print(" occupied slots:",count_o)
print("vacant slots",count_v)

#allocate  the first vacant slot
for i in range(len(parking)):
    if parking[i] == "Vacant":
        parking[i] = "Occupied"
        print("\nFirst Vacant Slot Allocated:", i + 1)
        break

# 4. Calculate parking occupancy percentage
occupied = 0

for status in parking:
    if status == "Occupied":
        occupied += 1

total_slots = len(parking)

occupancy_percentage = (occupied / total_slots) * 100

print("Parking Occupancy Percentage:",
      round(occupancy_percentage, 2), "%")

# 5. Store updated parking information in parking.txt
file = open("parking.txt", "w")

for i in range(len(parking)):
    file.write("Slot " + str(i + 1) + " : " +
               parking[i] + "\n")

file.close()

print("Updated parking information saved to parking.txt")
