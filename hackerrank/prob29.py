import string
alpha=[]
fv=[]
for i in range(0,52):
    alpha.append(string.ascii_letters[i])

def swap_case(s):
    valu=""
    for j in s:
        if(j.isalpha()==True):
            if(j.isupper()==True):
                valu=valu+j.lower()
            elif(j.islower()==True):
               valu=valu+j.upper()
        else:
           valu=valu+j
    return valu
if __name__ == '__main__':
    s = input()
    res=swap_case(s)
    print(res)