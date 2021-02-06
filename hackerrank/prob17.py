n=int(input(""))
if(n>=2 and n<=10):
  val=list(map(int,input().split()))
  for j in val:
      if(j>100 or j<-100):
          val=[]
  else:

   highest=max(val)
   runner=min(val)
   for j in range(0,len(val)):
     if((val[j]>=runner and val[j]!=highest)):
        runner=val[j]
   print(runner)






