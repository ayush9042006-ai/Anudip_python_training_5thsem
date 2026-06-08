'''4. Cricket Tournament Statistics 
Problem Statement 
Runs scored by players in a tournament
runs = {  "Virat": 645,     
       "Rohit": 512,     
       "Gill": 698,    
         "Rahul": 435,    
           "Hardik": 278,     
           "Pant": 534,     
           "Surya": 389,    
             "Jadeja": 301,    
               "Iyer": 455,    
                 "KL": 410 } 
Tasks 1. Display players scoring more than 500 runs. 
 2. Find the Orange Cap winner. 
   3. Find the lowest scorer. 
     4. Calculate total runs scored.  
     5. Create a list of players scoring below 400.  
     6. Count players scoring between 400 and 600 runs.'''


runs = {
    "Virat": 645,
    "Rohit": 512,
    "Gill": 698,
    "Rahul": 435,
    "Hardik": 278,
    "Pant": 534,
    "Surya": 389,
    "Jadeja": 301,
    "Iyer": 455,
    "KL": 410
}

# 1. Players scoring more than 500 runs......>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>..
print("Players scoring more than 500 runs...:")
for i in runs:
    if runs[i] > 500:
        print(i, ":", runs[i])

# 2. Orange Cap winner...................................................
orange = max(runs, key=runs.get)
print("Orange Cap Winner:")
print(orange, ":", runs[orange])

# 3. Lowest scorer.................................................
low = min(runs, key=runs.get)
print("lowest Scorer:")
print(low, ":", runs[low])

# 4. Total runs scored........................................
total = sum(runs.values())
print("Total Runs:", total)

# 5. Players scoring below 400........................................................
below= []
for i in runs:
    if runs[i] < 400:
        below.append(i)

print("players scoring below 400:")
print(below)

# 6. Count players scoring between 400 and 600...................................................
count = 0

for i in runs:
    if 400 <= runs[i] <= 600:
        count += 1

print("players scoring between 400 and 600:", count)