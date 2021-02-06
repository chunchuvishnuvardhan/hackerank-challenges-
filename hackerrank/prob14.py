v=input("")
def testing(vals):
    for k in range(0,len(vals)):
        if(vals[k]==',' and vals[k+1]==',' or vals[k]=='.' and vals[k+1]=='.' or vals[k]==',' and vals[k+1]=='.' or vals[k]=='.' and vals[k+1]==','):
            return False
    else:
     return True
def calculate(val):
 values = []
 for i in val:
    if(i==',' or i=='.'):
        pr(values)
        values=[]
    else:
        values.append(i)
        if(i==val[len(val)-1]):
            pr(values)
def pr(value):
    for j in value:
        print(int(j),end='')
res=testing(v)
if(res==False):
    print("")
else:
    calculate(v)


