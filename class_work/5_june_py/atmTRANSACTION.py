trans1=[5000,-2000,3000,-1000,-500,7000]
total_B=0
Balance=[]
total_d=0
deposite=[]
total_w=0
withdraw=[]


for i in trans1:
    total_B+=i
    Balance.append(i)

    if i >=0:
        total_d+=i
        deposite.append(i)
    else:
        total_w-=i
        withdraw.append(i)
print(f"current balance{Balance}")
print(f"Deposite..... {deposite}")
print(f"withdraw.....{withdraw}")
print(f"largest deposite...{max(trans1)}")
print(f"largest withdraw......{min(trans1)}")
