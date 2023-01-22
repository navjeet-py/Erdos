from math import factorial
mod = 3 ** 20
print(mod)

ans = 0

for i in range(1, 60):
    x = (i * i + i + 1) * factorial(i)
    ans += x
    ans %= mod

print(ans)

# ANSWER IS 3486784400.