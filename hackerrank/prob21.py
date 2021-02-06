

values=[]
n=int(input("enter n"))
li=['insert','print','remove','append','sort','pop','reverse']
for j in range(0,n):
    val=list(map(str,input('').split()))
    if(val[0]==li[0]):
      values.insert(int(val[1]),eval(val[2]))
    elif(val[0] == li[1]):
       print(values)
    elif (val[0] == li[2]):
       values.remove(eval(val[1]))
    elif (val[0] == li[3]):
        values.append(eval((val[1])))
    elif (val[0] == li[4]):
         values.sort()
    elif (val[0] == li[5]):
         values.pop(eval(val[1]))
    elif (val[0] == li[6]):
          values.reverse()

