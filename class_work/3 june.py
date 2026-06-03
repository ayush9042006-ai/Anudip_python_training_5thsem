import math as m1


side1= int(input("enter the side1 in cm=  "))
side2= int(input("enter the side2 in cm=  "))
side3= int(input("enter the side3 in cm=  "))

#parameter of traingle
parameter= side1 + side2 + side3
s=parameter/2
#area of triangle
area=m1.sqrt(s*(s-side1)*(s-side2)*(s-side3))
#display the result
print("area of given triangle",area)
print("parameter of triangle",parameter)