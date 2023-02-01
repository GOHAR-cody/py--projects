print("welcome to Health Management system")
def getdata():
    import datetime
    return datetime.datetime.now()
i=1
for i in range(i):
  print("I'm your trainer. Please enter your name...")            #adnan  or  farhan
  name=input()
  if name=='adnan':
   print("hey!adnan what you want ? 1-diet plan   2-exercise")        #input in numbers
   de=int(input())
   if de==1:
     print("do you want to 1-lock or  2-retrive")                       #input in numbers
     lr=int(input())
     if lr==1:
       with open("adnandiet.txt","a") as f:
        print("file opened!! enter your diet plan")
        f.write(input()+""+str([str(getdata())]))
     elif lr==2:
       with open("adnandiet.txt") as f:
         print(f.read()+""+str([str(getdata())]))
   elif de==2:
    print("1-log    2-retrive")
    lr=int(input())
    if lr==1:
     with open("adnanex.txt","a") as f:
      print("file opened!! enter your exercise plan")
      f.write(input()+""+str([str(getdata())]))
    elif lr == 2:
     with open("adnanex.txt") as f:
      print(f.read()+""+str([str(getdata())]))
  elif name=='farhan':
   print("hey!farhan what you want to see? 1-diet plan   2-exercise")
   de=int(input())
   if de==1:
     print("do you want to 1-lock  2-retrive")
     lr=int(input())
     if lr==1:
       with open("farhandiet.txt","a") as f:
        print("file opened!! enter your diet plan")
        f.write(input()+""+str([str(getdata())]))
     elif lr==2:
       with open("farhandiet.txt") as f:
         print(f.read()+""+str([str(getdata())]))
   elif de==2:
    print("1-log    2-retrive")
    lr=int(input())
    if lr==1:
     with open("farhanex.txt","a") as f:
      print("file opened!! enter your exercise plan")
      f.write(input()+""+str([str(getdata())]))
    elif lr == 2:
     with open("farhanex.txt") as f:
      print(f.read()+""+str([str(getdata())]))
  else:
   print("sorry you are not registered")
print("process completed")

