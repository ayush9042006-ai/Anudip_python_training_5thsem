dict1={
}
n=int(input("enter the no. of record in dict"))
for i in range(n):
    id= int(input("Enter Id number: "))
    salary= int(input(f"Enter salary of {i+1}: "))
    while salary < 0:
        print("re enter the salary...=")
        salary= int(input(f"Enter salary of {i+1}: "))
    else:
         dict1[id] = salary
print("final dictinory....>>>",dict1)

count=0
list=[]
for i in dict1:
    if dict1[i] > 30000:
        count+=1

    if dict1[i]<20000:
        list.append(dict1)
print(count)
print(list)