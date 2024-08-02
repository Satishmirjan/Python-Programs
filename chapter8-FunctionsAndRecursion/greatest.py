

def greatest(a,b,c):
  if(a>b and a>c):
    return a
  elif(b>c):
    return b
  else:
    return c
  


x=int(input("enter the first number  : "))
y=int(input("enter the second number : "))
z=int(input("enter the third number : "))
ans=greatest(x,y,z)
print("the greatest number is ",ans)