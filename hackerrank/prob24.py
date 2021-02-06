# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n=int(input(""))
list=[]
regex = '[+-]?[0-9]+\.[0-9]+'

# Define a function to
# check Floating point number
def check(floatnum):
    # pass the regular expression
    # and the string in search() method
     if (re.search(regex, floatnum)):
        print("True")
     else:
        print("False")
for i in range(0,n):
    val=input("")
    list.append(str(val))
for j in list:
    print(j)
    check(j)
