# to read and display the data 
#1. number of viwels in file
# 2. no of charaters into the file
# 3. no of lines into the file


file2=open("student.txt",'r')
read=file2.read()
c=0
c1=0
line=0
for i in read:
    if i in "aeiouAEIOU":
        c+=1
    if i !='\n':
        c1+=1
    else:
        line+=1
print(f"no of vowels{c}")
print(f"no of charater :{c1}")
print(f"no of lines :{line}")