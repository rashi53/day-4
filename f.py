fo=open(r"c:\python\student.txt","w")#a
count=0
while count<5:
 str1=input("enter the txt:")#raw input
 fo.write(str1+'\n')
 count=count+1
fo.close()
print("work done")
