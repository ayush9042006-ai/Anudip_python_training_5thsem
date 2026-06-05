a = int(input("Enter the number of players >>> "))

total = 0
#TO CHECK THE USER DO NOT TAKE NEGATIVE NUMEBR:
if a <= 0:
    print("Player count cannot be negative or zero")
    a = int(input("RE-Enter the number of players >>> "))
#ENTERY OF SCORE 
for i in range(1, a + 1):
    score = int(input(f"Score of player {i}: "))
    # TO CHECK WHEATHER SCORE SHOULD NOT BE NEGATIVE:
    while score < 0:
        print("Invalid score!")
        score = int(input(f"Enter the score again for player {i}: "))

    total += score
#TOTAL score
print("Total score of all players =", total)
 