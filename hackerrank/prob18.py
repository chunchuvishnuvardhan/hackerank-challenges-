n=int(input(""))
lnames=[]
lscores=[]
for i in range(0,n):
    names=input("enter name")
    scores=float(input("enter values"))
    lnames.append(names)
    lscores.append(scores)
runner=max(lscores)
secondrunner=runner
res={ }
for key in range(0,len(lnames)):
    for value in range(0,len(lscores)):
       if(key==value):
        res[lnames[key]] = lscores[value]


for j in range(0, len(lscores)):
   if(lscores[j]<runner):
       secondrunner=runner
       runner=lscores[j]
   elif(lscores[j] < secondrunner and lscores[j] != runner):
     secondrunner=lscores[j]

final=[]
for k in res:
    if(res[k]==secondrunner):
            final.append(k)
final.sort()
for i in final:
    print(i)








