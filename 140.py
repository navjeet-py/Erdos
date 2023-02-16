from math import gcd
from sympy.ntheory.factor_ import totient


def P(N):
    ans = 1
    for i in range(1, N + 1):
        if gcd(i, N) == 1:
            ans *= i
    return ans % N

def F(N):
    ans = 0
    for i in range(1, N + 1):
        ans += P(i)
    return ans

for i in range(1, 7):
    print(i, F(10**i))
