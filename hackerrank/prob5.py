year=int(input(""))

def is_leap(year):
      if (year >= 1900 and year <= 10 ** 5):
        if((year%4==0 or year%400==0) and (year%100!=0)):
          return True
        else:
          return False

val=is_leap(year)
print(val)