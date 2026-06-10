text=open("sentence.txt","r")
dest=open("student.txt","w")

t=text.read()
dest.write(t)
print("copied succesfully:::")
text.close()
dest.close()