s=input("enter s")
k=input(" enter k")
val=len(k)
list=[]
if((len(s)>0 and len(s)<100)and(len(k)>0 and len(k)<len(s))):
   for i in range(0,len(s)):
    str=s[i:i+val]
    list.append(str)
    if(k==str):
        print((i, i+val-1))
   if(k  not in list):
       print((-1, -1))







