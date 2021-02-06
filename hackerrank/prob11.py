def func(temp, l):
    global m_sum, m
    if len(l) == 0:
        if temp > m_sum: m_sum = temp % m
        return
    for i in range(len(l[0])):
        crap = ((temp % m) + ((l[0][i] ** 2) % m)) % m
        func(crap, l[1:])

k, m = map(int, input().split())
l = []
for _ in range(k):
    l.append(map(int, input().split())[1:])

m_sum = 0
temp = 0
for i in range(len(l[0])):
    temp = (l[0][i] ** 2) % m
    func(temp, l[1:])

print(m_sum)



t=int(input("enter the no fo test cases"))
def calculate(values):
    if(values[0][0]==values[1][0] and values[0][1]==values[1][1] and values[0][2]==values[1][2] and values[0][3]==values[1][3] and values[0][4]==values[1][4]):
        substract=int(values[0][5])-int(values[1][5])
        hours=substract//100
        minutes=substract%100
        totaltime=hours*3600+minutes*60
        print(totaltime)
    else:

        timegap=int(values[0][5])-int(values[1][5])
        hours1=int((values[0][4].split())[0:2])*3600+int((values[0][4].split())[3:5])*60+int(values[0][4])[6:8]
        hours2=int((values[1][4].split())[0:2])*3600+int((values[1][4].split())[3:5])*60+int(values[1][4])[6:8]
        if(hours1>=hours2):
            hourst=hours1-hours2
        else:
            hourst=hours2-hours1
        if(int(values[0][1])>int(values[1][1])):
         daysgap = int(values[0][1] - values[1][1]) * 24 * 60 * 60
        else:
            daysgap = int(values[1][1] - values[0][1]) * 24 * 60 * 60

        totaltime=daysgap+hourst
        hou=timegap//100
        min=timegap%100
        tt=hou*3600+min*60
        print(totaltime-tt)

for i in range(0,t):
   values=[]
   for j in range(0,2):
    arr = list(map(str, input(' ').split()))
    values.append(arr)
   calculate(values)
dict={1:'jan',2:'feb',3:'mar',4:'apr',5:'may',6:'jun',7:'jul',8:'aug',9:'sep',10:'oct',11:'nov',12:'dec'}
dict1={31:'jan',28:'feb',31:'mar',30:'apr',31:'may',}