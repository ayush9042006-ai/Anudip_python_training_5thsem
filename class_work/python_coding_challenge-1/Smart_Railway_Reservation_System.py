'''Problem 1: Smart Railway Reservation System 
Problem Statement
 A railway reservation system stores the booking status of seats in a train coach. Sample Data 
 seats = { 1: "Booked", 2: "Available", 3: "Booked", 4: "Available",5: "Booked", 6: "Booked",    
        7: "Available", 8: "Booked", 9: "Available",10: "Booked" } 
Tasks 1. Display all available seat numbers.
      2. Count booked and available seats.  
      3. Reserve the first available seat.  
      4. Cancel booking for a given seat number.  
      5. Store the updated reservation status in reservations.txt.  
      6. Display occupancy percentage.  '''


seats = {    
     1: "Booked",     
     2: "Available",    
       3: "Booked",    
         4: "Available",    
           5: "Booked",     
           6: "Booked",     
           7: "Available",    
             8: "Booked",    
               9: "Available",     
               10: "Booked" } 

print("Available seats")
for no , value in seats.items():
    if value == "Available":
        print(no,end= " ")


count_b=0
count_a=0
for value in seats.values():
    if value=="Booked":
        count_b+=1
    else:
        count_a+=1

print("\nbooked seats :",count_b)
print("Available seats :",count_a)

for keys,value in seats.items():
    if value =="Available":
        print("seat",keys,"Reserved successfully")
        break


# 4. Cancel booking for a given seat number
seat = int(input("\nEnter seat number to cancel booking: "))

if seat in seats:
    seats[seat] = "Available"
    print("Booking Cancelled for Seat", seat)
else:
    print("Invalid Seat Number")

# 5. Store updated reservation status in reservations.txt
file = open("reservations.txt", "w")

for seat_no, status in seats.items():
    file.write(str(seat_no) + "," + status + "\n")

file.close()

print("\nUpdated reservation status saved to reservations.txt")

# 6. Display occupancy percentage
booked = 0

for status in seats.values():
    if status == "Booked":
        booked += 1

total_seats = len(seats)

occupancy = (booked / total_seats) * 100

print("Occupancy Percentage:", round(occupancy, 2), "%")
