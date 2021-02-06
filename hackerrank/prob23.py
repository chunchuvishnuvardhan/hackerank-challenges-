x=int(input("enter x"))
y=int(input("enter y"))
z=int(input("enter z"))
n=int(input("enter z"))
list=[]
smalllist=[]
for i in range(0,x+1):
    for j in range(0,y+1):
        for k in range(0,z+1):
            if(i+j+k!=n):
                smalllist.append(i)
                smalllist.append(j)
                smalllist.append(k)
                list.append(smalllist)
                smalllist=[]

print(list)