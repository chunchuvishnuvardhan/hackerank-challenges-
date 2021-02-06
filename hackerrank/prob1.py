n=int(input("enter the n value"))
if(n>=1 and n<=100):

 if(n%2!=0):
    print("weird")
 elif(n%2==0 and (n>=2 and n<=5)):
    print("not weird")
 elif(n%2==0 and (n>=6 and n<=20)):
    print("weird")
 elif(n%2==0 and n>20):
   print("not weird")
else:
    print("number not in range")