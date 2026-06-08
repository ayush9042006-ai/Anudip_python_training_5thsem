# wap to input a sentence and display the frequency of vowels which are present in the given sentence

s = input("Enter a sentence: ")
f1=0
f2=0
f3=0
f4=0
f5=0
for i in s:
    if i in 'aA':
        f1+=1
    elif i in 'eE':
        f2+=1
    elif i  in 'iI':
        f3+=1
    elif i in 'oO':
        f4+=1
    elif i in 'uU':
        f5+=1
if f1 > 0:
    print("a :",f1)
if f2 >0:
    print("e :",f2)
if f3 > 0:
    print("i :",f3)
if f4 > 0:   
    print("o :",f4)
if f5 > 0:  
    print("u :",f5)