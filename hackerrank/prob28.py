import math
tl=[]
abl=[]
bcl=[]
cdl=[]
dif=[]
x=[]
y=[]
def ab(a,b):
    for i in range(0,3):
        abl.append(a[i]-b[i])
    print(abl)
def bc(a,b):
    dif=[]
    for i in range(0,3):
       bcl.append(a[i]-b[i])
    print(bcl)
def cd(a,b):
    for i in range(0,3):
        cdl.append(a[i]-b[i])
    print(cdl)
def crossx(li1,li2):
        x.append(li1[1]*li2[2]-li2[1]*li1[2])
        x.append(li1[0]*li2[2]-li2[0]*li1[2])
        x.append(li1[0]*li2[1]-li2[0]*li1[1])
def crossy(li1,li2):
    y.append(li1[1] * li2[2] - li2[1] * li1[2])
    y.append(li1[0] * li2[2] - li2[0] * li1[2])
    y.append(li1[0] * li2[1] - li2[0] * li1[1])

def dotxy(li1,li2):
    dotprod=li1[0]*li2[0]+li1[1]*li2[1]+li1[2]*li2[2]
    print(dotprod)
    return dotprod


for j in range(0,4):
    val=list(map(eval,input("").split()))
    tl.append(val)
print(tl)
ab(tl[0],tl[1])
bc(tl[1],tl[2])
cd(tl[2],tl[3])
crossx(abl,bcl)
crossy(bcl,cdl)
print(x)
print(y)

def magn(x):
    sx=0
    for i in range(0,3):
        sx=(x[i])**2+sx
    print(math.sqrt(sx))
    return math.sqrt(sx)

fv=dotxy(x,y)/(magn(x)*magn(y))
print(round(math.acos(fv)*57.29,2))







