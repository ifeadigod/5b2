from ast import And
from re import X


# a = 30
# b= 15
# c = 12
# equation = a**n + b**n = c**n
# check = map(lambda x: (a**n), equation)

def _femhat(a,b,c,n):
    if n > 2 and a**n + b**n is c**n:
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No!, That doesn't work")
    
a = int(input("write a  value\n"))
b = int(input("write a value\n"))
c = int(input("write a value\n"))
n = int(input("write a value\n"))

print(_femhat(12,14,22,2))



# print(x)print(sum(a**n, b**n))