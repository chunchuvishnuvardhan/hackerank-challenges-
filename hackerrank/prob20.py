n=int(input(""))
dictiona={}
if(n>=2 and n<=10):
  for i in  range(0,n):
    val=list(map(str,input('').split()))
    if(len(val)-1==3):
     dictiona[val[0]]=val[1:]
  que=input("")
  sum=0
  for i in dictiona[que]:
   if(int(i)<=100 and int(i)>=0):
     sum=sum+int(i)
   else:
       sum=0
  aver=sum/len(dictiona[que])
  print(round(aver,1))
