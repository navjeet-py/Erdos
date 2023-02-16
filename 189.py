"""
1, 2, 3, 4, 5, 6, 7, 8, 9, 10
we will have to kill at least n/2 bigger people for sure.
if we kill 6, 7,  8, 9, 10
1, 2, 3,  4, 5 will also be dead.

So, if we will kill bigger half, rest half will also be dead.
For odd, we also need to kill the middle term.
"""

# ANSWER IS 61728395.

p = "(a+b+3)^2+(a+2b+5/2+2)^2 = 100, (2a-2b)^2+(2a+1-4b-4)^2=3600"
p = p.replace('a', 'x')
p = p.replace('b', 'y')
print(p)

def f(a, b):
    return 2*a*b+3*a+3*b+9/2

print(f(-9.1035859148285260167, 7.267792908955394508) * 3)
from math import factorial

x = factorial(400)
while x % 10 == 0:
    x //= 10

print(str(x)[-5:])