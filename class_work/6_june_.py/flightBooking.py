# Flight booking records
bookings = ( ("P101", "Delhi", "Confirmed"),
    ("P102", "Mumbai", "Waiting"),
    ("P103", "Delhi", "Confirmed"),
    ("P104", "Chennai", "Cancelled"),
    ("P105", "Mumbai", "Confirmed"),
    ("P106", "Delhi", "Waiting")
)

#Display Confirmed Passengers
print("Confirmed Passengers:")
for booking in bookings:
    if booking[2] == "Confirmed":
        print(booking[0], booking[1])

#Count passengers travelling to Delhi
delhi_count = 0
for booking in bookings:
    if booking[1] == "Delhi":
        delhi_count += 1

print("PassengersTravelling to Delhi.......:", delhi_count)

#Count booking status
confirmed = 0
waiting = 0
cancelled = 0

for booking in bookings:
    if booking[2] == "Confirmed":
        confirmed += 1
    elif booking[2] == "Waiting":
        waiting += 1
    elif booking[2] == "Cancelled":
        cancelled += 1

print("\nConfirmed:", confirmed)
print("Waiting:", waiting)
print("Cancelled:", cancelled)

# Task 4: Create waiting list
waiting_list = []

for booking in bookings:
    if booking[2] == "Waiting":
        waiting_list.append(booking[0])

print("\nWaiting List:", waiting_list)

# Task 5: Find most booked destination
delhi = 0
mumbai = 0
chennai = 0

for booking in bookings:
    if booking[1] == "Delhi":
        delhi += 1
    elif booking[1] == "Mumbai":
        mumbai += 1
    elif booking[1] == "Chennai":
        chennai += 1

if delhi > mumbai and delhi > chennai:
    most_booked = "Delhi"
elif mumbai > delhi and mumbai > chennai:
    most_booked = "Mumbai"
else:
    most_booked = "Chennai"

print("



