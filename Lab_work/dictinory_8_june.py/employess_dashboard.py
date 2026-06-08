'''2. Employee Performance Dashboard Problem Statement Employee performance scores are stored as:
 performance = {     "EMP101": 92,    
   "EMP102": 78,    
     "EMP103": 45,    
       "EMP104": 88,   
           "EMP105": 97,    
             "EMP106": 56,    
               "EMP107": 81,   
                   "EMP108": 64,    
                     "EMP109": 39,  
                           "EMP110": 73}
 Tasks 1. Display employees scoring above 80.  
 2. Count employees needing improvement (score < 60). 
   3. Find the top performer.  
   4. Calculate average performance score. 
     5. Create separate lists:  o Excellent (≥ 90)  o Good (75–89)  o Average (60–74)  o Poor (< 60) ''' 


performance = {
    "EMP101": 92,
    "EMP102": 78,
    "EMP103": 45,
    "EMP104": 88,
    "EMP105": 97,
    "EMP106": 56,
    "EMP107": 81,
    "EMP108": 64,
    "EMP109": 39,
    "EMP110": 73
}

# 1. Employees scoring above 80.....................................
print("Employees scoring above 80..:")
for i in performance:
    if performance[i] > 80:
        print(i, ":", performance[i])

# 2. Count employees needing improvement
count = 0
for i in performance:
    if performance[i] < 60:
        count += 1

print("Employees needing improvement.............:", count)

# 3. Find the top performer
top = max(performance, key=performance.get)
print("Top Performer........:")
print(top, ":", performance[top])

# 4. Calculate average performance score
total = sum(performance.values())
average = total / len(performance)

print("Average Performance Score:", average)

# 5. Separate lists
excellent =[]
good =[]
average =[]
poor =[]

for i in performance:
    score = performance[i]

    if score >= 90:
        excellent.append(i)
    elif score >= 75:
        good.append(i)
    elif score >= 60:
        average.append(i)
    else:
        poor.append(i)

print("Excellent Employees:", excellent)
print("Good Employees:", good)
print("Average Employees:", average)
print("Poor Employees:", poor)