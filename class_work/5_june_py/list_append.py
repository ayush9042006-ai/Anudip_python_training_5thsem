# WAP to create the list of 20 no. given  by user
# ask the user to input any other number
# remove all the dplicate entries of this number from the list

n =int(input("Enter the size of list: "))

lst=[]

for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    lst.append(element)

print(lst)

value=int(input("Enter the element: "))

count=lst.count(value)
if count==0:
        print("element not found...")
elif count==1:
        print("no duplicate value fount in list")
else:
    lst.reverse()
    for i in range(1,count):
            lst.remove(value)
# reverse the list again
    lst.reverse()
    print("after remove element")
    print(lst)


