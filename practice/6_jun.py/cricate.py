'''scores = { 
    "Virat": 78, 
    "Rohit": 112, 
    "Gill": 45, 
    "Rahul": 89, 
    "Hardik": 32, 
    "Jadeja": 61, 
    "Surya": 105, 
    "Pant": 95, 
    "Bumrah": 18, 
    "Shami": 25 
} 
Tasks 
• Display players who scored 50 or more runs.  
• Count the number of centuries.  
• Find the player with the highest score.  
• Create a list of players scoring below 30 runs.  
• Determine how many players scored between 50 and 99. '''

scores = {
    "Virat": 78,
    "Rohit": 112,
    "Gill": 45,
    "Rahul": 89,
    "Hardik": 32,
    "Jadeja": 61,
    "Surya": 105,
    "Pant": 95,
    "Bumrah": 18,
    "Shami": 25
}

# Players scoring 50 or more runs
print("Players scoring 50 or more runs:")
for player in scores:
    if scores[player] >= 50:
        print(player)

# Count centuries
centuries = 0
for player in scores:
    if scores[player] >= 100:
        centuries += 1

print("Number of centuries =", centuries)

# Highest scorer
highest_score = 0
highest_player = ""

for player in scores:
    if scores[player] > highest_score:
        highest_score = scores[player]
        highest_player = player

print("Highest Scorer =", highest_player)
print("Score =", highest_score)

# Players scoring below 30 runs
low_scores = []

for player in scores:
    if scores[player] < 30:
        low_scores.append(player)

print("Players scoring below 30 runs:")
print(low_scores)

# Players scoring between 50 and 99
count = 0

for player in scores:
    if scores[player] >= 50 and scores[player] <= 99:
        count += 1

print("Players scoring between 50 and 99 =", count)