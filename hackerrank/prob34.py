n,m = map(int, input().split())
arr=list(map(int,input("").split()))
values=[]
happines=0
for i in range(0,2):
    mvals=list(map(int,input("").split()))
    values.append(mvals)
test=0
print(arr)
print(values)
if((n>=1 and n<=10**5) and (m>=1 and m<=10**5)):
 if((min(arr)>=1 and max(arr)<=10**9) and ((min(values[0])>=1 and max(values[0])<=10**9)) and (min(values[1])>=1 and max(values[1])<=10**9)):
  for j in arr:
    for l in values:
        if(j in values[0]):
           happines=happines+1
        elif(j in values[1]):
            happines=happines-1
        else:
            happines=happines

print(happines-1)

