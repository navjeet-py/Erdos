from sympy.ntheory.factor_ import totient

def phi(n):
    return int(totient(n))

for i in range(4, 10000):
    if phi(i + 2) == phi(i + 1) == phi(i):
        print(i, i % 1729)

