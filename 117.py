from math import factorial

def binomial(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

M = 100
N = 20

def count_with_minimum(x):
    ans = 0
    for i in range(1, N + 1):
        ans += (binomial(N, i) * ((M - x) ** (N - i)))
    return ans

total = 0
cnt = 0
for i in range(1, 101):
    x = count_with_minimum(i)
    cnt += x
    total += (x * i)
print((total / cnt) * 10**6)

# ANSWER IS 5278561.