
def f(n):
    xor = 0
    for i in range(1, 2 ** n + 1):
        xor ^= i
    return xor

for i in range(1, 10):
    print(i, f(i))

print(pow(2, 2013, 10 ** 9 + 7))