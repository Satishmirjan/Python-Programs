li=[]
i=0
print("enter the elements")


while(i<8):
  a=int(input())
  li.append(a)
  i+=1

unique_li=set(li)

print(unique_li)