# Star Pattern(Ascending & Descending) in Python
print("enter the number of lines")
 n=int(input())
 i=0
 j=0                                 
 bool(n)
 if n>=0:
  for i in range(n):
   for j in range(i+1):
     print("*",end="")
   print()
 else:
  for i in range(n):
   for j in range(n-i):
     print("*",end="")
   print()
