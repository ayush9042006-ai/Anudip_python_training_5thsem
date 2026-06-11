'''Problem 7: Movie Ticket Booking System 
Problem Statement 
Seat booking status in a cinema hall is stored as follows. 
Sample Data tickets = {"A1": "Booked","A2": "Available",    
                 "A3": "Booked",   
                 "A4": "Available",    
                 "B1": "Booked",     
                 "B2": "Available",    
                 "B3": "Booked",     
                 "B4": "Available",     
                 "C1": "Booked",     
                 "C2": "Available" } 
Tasks 1. Display available seats.  
2. Count booked and available seats.  
3. Reserve the first available seat.  
4. Save updated booking details to tickets.txt.  
5. Calculate hall occupancy percentage'''


# Movie Ticket Booking System

tickets = {
    "A1": "Booked",
    "A2": "Available",
    "A3": "Booked",
    "A4": "Available",
    "B1": "Booked",
    "B2": "Available",
    "B3": "Booked",
    "B4": "Available",
    "C1": "Booked",
    "C2": "Available"
}

# 1. Display Available Seats
print("AVAILABLE SEATS")

for seat, status in tickets.items():
    if status == "Available":
        print(seat)

# 2. Count Booked and Available Seats
booked = 0
available = 0

for status in tickets.values():
    if status == "Booked":
        booked += 1
    else:
        available += 1

print("\nBooked Seats :", booked)
print("Available Seats :", available)

# 3. Reserve the First Available Seat
for seat in tickets:
    if tickets[seat] == "Available":
        tickets[seat] = "Booked"
        print("\nFirst Available Seat Reserved :", seat)
        break

# 4. Save Updated Booking Details to File
file = open("tickets.txt", "w")

for seat, status in tickets.items():
    file.write(seat + "," + status + "\n")

file.close()

print("Updated booking details saved to tickets.txt")

# 5. Calculate Hall Occupancy Percentage
booked = 0

for status in tickets.values():
    if status == "Booked":
        booked += 1

total_seats = len(tickets)

occupancy = (booked / total_seats) * 100

print("Hall Occupancy Percentage :", round(occupancy, 2), "%")