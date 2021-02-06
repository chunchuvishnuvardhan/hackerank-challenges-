def print_rangoli(n):
    # your code goes here
    val = 96 + n
    x = n - 1
    if (n > 0 and n < 27):
        for i in range(0, n * 2 - 1):
            spaces = n - i - 1
            spaces2 = i - n + 1
            for j in range(0, n * 2 - 1):
                if (i <= n-1):
                    if (spaces == 0):
                        if (i + j == n - 1 or j <= n + i - 1):
                            if (i + j == n - 1 or j == n + i - 1):
                                val = 96 + n
                                if(i+j==n-1):
                                   if(i==0):
                                     print(chr(val),end="")
                                   else:
                                     print(chr(val), end="-")
                                else:
                                    print(chr(val),end="")
                            elif (j <= n - 1):
                                val = val - 1
                                print(chr(val), end="-")
                            elif (j > n - 1 and j != (n + i - 1)):
                                val = val + 1
                                print(chr(val), end="-")
                            else:
                                   print("-",end="-")
                        else:
                            print("-", end="-")
                    else:
                        spaces = spaces - 1
                        print("-", end="-")
                else:
                    if (spaces2 == 0):
                        if (j == (i - n + 1) or j <= (((n - 1) * 2) - (i - n + 1))):
                            if (j == i - n + 1 or j == (((n - 1) * 2) - (i - n + 1))):
                                val = 96 + n
                                if(j==i-n+1):
                                  if(i==2*n-2):
                                    print(chr(val), end="")
                                  else:
                                      print(chr(val),end="-")
                                else:
                                    print(chr(val),end="")
                            elif (j <= (n - 1)):
                                val = val - 1
                                print(chr(val), end="-")
                            elif (j > n - 1 and j != (((n - 1) * 2) - (i - n + 1))):
                                val = val + 1
                                print(chr(val), end="-")
                        else:
                            print("-", end="-")
                    else:
                        spaces2 = spaces2 - 1
                        print("-", end="-")
            print("\r")
    else:
        print("")


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)


