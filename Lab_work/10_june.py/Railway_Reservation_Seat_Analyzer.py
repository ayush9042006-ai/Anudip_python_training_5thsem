'''1. Railway Reservation Seat Analyzer 
Problem Statement 
A railway coach has seats represented as follow: 
seats = ["Booked", "Available", "Booked", "Booked","Available", "Available", "Booked", "Available","Booked", "Booked", "Available", "Booked" ] 
Requirements Create the following functions: 
1. count_seats(seats) Returns the number of booked and available seats. 
2. first_available(seats) Returns the seat number of the first available seat. 
3. occupancy_percentage(seats) Returns the percentage of occupied seats.
4. display_available_seats(seats) Displays all available seat numbers.'''



# Railway Reservation Seat Analyzer

seats = [ "Booked","Available","Booked","Booked","Available","Available","Booked","Available","Booked","Booked","Available","Booked"]

#1: Count booked and available seats.........................................................
def count_seats(seats):
    book= seats.count("Booked")
    available= seats.count("Available")
    return book, available
# 2: Find first available seat...............................................................
def first_available(seats):
    for i in range(len(seats)):
        if seats[i] == "Available":
            return i + 1      # Seat numbers start from 1
    return "No seat available"

#3: Calculate occupancy percentage............................................................
def occupancy_percentage(seats):
    book= seats.count("Booked")
    total= len(seats)
    per= (book/ total) * 100
    return per

#4: Display all available seat numbers..............................................................
def display_available_seats(seats):
    print("Available Seat Numbers:")
    for i in range(len(seats)):
        if seats[i] == "Available":
            print(i + 1, end=" ")
    print()
booked, available = count_seats(seats)
print("Booked Seats :", booked)
print("Available Seats :", available)
print("First Available Seat :", first_available(seats))
print("Occupancy Percentage :", round(occupancy_percentage(seats), 2), "%")
display_available_seats(seats)