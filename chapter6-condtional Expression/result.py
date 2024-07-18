li=[]

print("enter the marks in 3 subject :  ")
i=0
while(i<3):
  li.append(int(input()))
  i+=1
sum=0
for l in li:
  sum+=l
 
  if(l<33):
    print("sorry ! you failed \n better luck next time")
    exit()


if((sum)/3<40):
 print("sorry ! you failed \n better luck next time")
 exit()

print("congratulation you passed ")
