from math import factorial


def binomial(n, c):
    return factorial(n) // (factorial(c) * factorial(n - c))

ans = 0
for i in range(1, 5):
    x = binomial(5, i) * (8 ** (5 - i) - 4 ** (5 - i))
    ans += x


print((ans / (9 ** 5)) * 59049)

# ANSWER IS 24180.