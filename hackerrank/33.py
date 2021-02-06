s=input("")
if(len(s)>0 and len(s)<1000):
    def alphanumeric(val):
        sum=0
        for j in val:
            if(j.isalpha()):
                sum=sum+1
            elif(j.isdigit()):
                sum=sum+1
        if(sum>=2):
            return True
        else:
            return False
    def alpha(val):
      for j in val:
        if(j.isalpha()):
            return True
            break
      else:
            return False
    def digits(val):
        for j in val:
            if (j.isdigit()):
                return True
                break
        else:
            return False
    def low(val):
        for j in val:
            if (j.islower()):
                return True
                break
        else:
            return False
    def high(val):
        for j in val:
            if (j.isupper()):
                return True
                break
        else:
            return False
print(alphanumeric(s))
print(alpha(s))
print(digits(s))
print(low(s))
print(high(s))

if((min(arr)>=1 and max(arr)<=10**9) and ((min(values[0])>=1 and max(values[0])<=10**9)) and (min(values[1])>=1 and max(values[1])<=10**9)):
 if(test==0):
   print(happines)
