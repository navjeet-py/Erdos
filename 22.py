from sympy.ntheory.factor_ import totient
from math import log10

def phi(x):
    return int(totient(x))

X = -1
for x in range(10**8, 10**9):
    if phi(x) == 10**8:
        X = x
        print(x)
        break

"""The number is 100064101. Now we need to find number of digits in its factorial.
log(n!) = log(1) + log(2) + ... log(n)
int(log(x) + 1) = number of digits in x.
"""

sm = 0

for i in range(1, X + 1):
    sm += log10(i)
print(sm)

# Answer is 757083374