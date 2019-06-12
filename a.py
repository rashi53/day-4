fo=open(r"c:\python\student.txt","a")#try with append mode"a"
while True:
    str1=input("enter the text:")
    fo.write(str1+'\n')
   #fo.write(r"\n")
    choice=input("to exit type x:")
    if choice=='x' or choice=='X':
      break
    else:
      continue
fo.close()
print("work done")
