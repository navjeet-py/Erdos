# WE HAVE TO FIND 10000 C 10000 mod 10**9+7

fac = 1
mod = 10 ** 9 + 7
for i in range(1, 10001):
    fac *= i
    fac %= mod
print(fac)
