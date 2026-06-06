score=[45,78,12,100,67,8,90,55]



# count half and full centuries
count_h=0
count_f=0
for i in score:
    if i ==50:
        count_h+=1

    if i==100:
        count_f+=1
print("count of half centuries..:",count_h)
print("count of full centuries..:",count_f)
print(f"highest....:{max(score)}")
# display score below than 20
for i in score:
    if i < 20:
        print("score below than 20:::",i)

#average of score
a=sum(score)
avg=a/len(score)
print(avg)
