n=int(input(""))
l2=[]
length=0
if(n>=1 and n<=10**5):
  for i in range(0,n):
    values=input("enter")
    l2.append(values.lower())
    length=length+len(values)
c=0
if(length<=10**6):
    l3=[]
    for k in range(0,len(l2)):
        if(l2[k]  not in l3):
            l3.append(l2[k])

    print(len(l3))
    for m in range(0,len(l3)):
        print(l2.count(l3[m]),end=" ")








