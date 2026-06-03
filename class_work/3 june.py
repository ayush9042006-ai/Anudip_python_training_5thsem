# import math as m1


# side1= int(input("enter the side1 in cm=  "))
# side2= int(input("enter the side2 in cm=  "))
# side3= int(input("enter the side3 in cm=  "))

# #parameter of traingle
# parameter= side1 + side2 + side3
# s=parameter/2
# #area of triangle
# area=m1.sqrt(s*(s-side1)*(s-side2)*(s-side3))
# #display the result
# print("area of given triangle",area)
# print("parameter of triangle",parameter)











''' programe which convert time in seconds into hours and minutes'''
t=int(input("enter time in seconds="))
if(t<0):
    exit("Time cannot be negative.....Exited")

print("................................")
hours=0
minutes=0

'''convert into hours'''
if(t>=3600):
    hours=t//3600
    remaningSeconds=t%3600
#................................
'''converts into  minutes'''
if(t>=60):
    minutes=t//60
    seconds=t%60
#................................
'''display the results'''
    
    
print("hours =",hours)
print("minutes =",minutes)
print("seconds =",t)