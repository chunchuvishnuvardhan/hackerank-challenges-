n=int(input("enter"))
lnames=[]
lscores=[]
secondunner=0
for i in range(0,n):
    scores=eval(input(""))
    lscores.append(scores)
runner=max(lscores)
secondrunner=runner
dif=0
lowest=min(lscores)
for j in range(0, len(lscores)):
   if(lscores[j]<runner):
       secondrunner=runner
       runner=lscores[j]
   elif(lscores[j] < secondrunner and lscores[j] != runner):
     secondrunner=lscores[j]
print(secondrunner)