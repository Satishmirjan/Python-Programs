dict={}

Key=""
value=""
print("Enter the key and value :  ")
i=0
while(i<4):
  key=input("enter the key: ")
  value=input("enter the value for key : ")
  dict.update({key:value})
  i=i+1

print(dict)