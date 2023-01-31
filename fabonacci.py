#Fabonacci series
def fabunachi(n):
  n1=0
  n2=1
  sum=0
  if n==1:
      print(n1)
  else:
      print(n1)
      print(n2)
      for i in range(n) :
       sum=n1+n2
       n1=n2
       n2=sum
       print(sum)

n=int(input("enter number"))
print(fabunachi(n))
