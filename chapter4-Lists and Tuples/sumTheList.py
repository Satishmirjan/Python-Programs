
li=[]

print("enter the 4 numbers")

index=0
while(index<4):
  li.append(int(input()))
  index=index+1
sum=0
for l in li:
  sum+=l


print("the sum of 4 number is : ",sum)