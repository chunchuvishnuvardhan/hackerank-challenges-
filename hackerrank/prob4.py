n=int(input(""))
if(n>=1 and n<=20):
    for i in range(0,n):
        print(i*i,end='\n')
else:
    print('out of range')