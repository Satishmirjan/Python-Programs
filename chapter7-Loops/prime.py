n=int(input("enter the number :  "))
i=2
while(i<n/2):
  if(n%i==0):
   print("not a prime number ")
   exit()
  i+=1

print("its a prime number ")