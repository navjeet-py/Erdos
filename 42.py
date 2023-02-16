"""


"""
"""
a1+a2+...+a10000 = 10000
binomial(19999, 9999)
"""

mod = 10**9 + 7

n = 19999
r = 9999

num = 1
for i in range(1, n + 1):
    num *= i
    num %= mod

den = 1
for i in range(1, r + 1):
    den *= i
    den %= mod
for i in range(1, n - r + 1):
    den *= i
    den %= mod
ans = num * pow(den, mod - 1, mod)
ans %= mod
print(ans)
