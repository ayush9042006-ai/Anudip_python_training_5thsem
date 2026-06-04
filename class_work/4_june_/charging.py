
import time
 
init = int(input("enter the battry percentage..."))
check = input("YES if pluged in , NO if not ")
 
if check.lower() == "yes":
    print("charging started 😉😉")
    while init != 100:
        print(f"the battery percentage is {init} %")
        time.sleep(2)
        init = init+10
 
    else:
        print("battery is fully charged !")
 
else:
    print("charger not connected!")