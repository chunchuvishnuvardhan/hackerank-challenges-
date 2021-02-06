import string
s=input("")
list=[]
values=[]
vowels=['a','e','i','o','u','A','E','I','O','U']
for i in string.ascii_letters:
 values.append(i)
print(values)

def pri(values):
    print()

for i in range(0,len(s)):
    if(s[i] in values):
        list.append(s[i])
for k in range(0,len(list)):
  for j in range(0,len(list)-1):
     if(list[j+k]):





