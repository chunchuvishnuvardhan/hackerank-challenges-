str1=str(input(""))
str2=input("")
print(str1)
print(str2)
values=[]
l=len(str2)
for i in range(0,len(str1)):
  if(i+1<=len(str1)):
    values.append(str1[i:i+l])
print(values.count(str2))