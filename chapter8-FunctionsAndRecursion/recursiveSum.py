def sum(n):
  if(n<=1):
    return 1

  return n+sum(n-1)
  

num=int(input("enter the number :  "))

ans=(sum(num))
print(f"The sum of first {num} is  {ans}")