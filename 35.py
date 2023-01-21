"""
It should also be written in the problem that
 'Different characters represent different digits.'
"""
from math import gcd

class Fraction:
    n = 0
    d = 1
    def __init__(self, n, d):
        self.n = n
        self.d = d
    def __add__(self, other):
        n1 = other.n
        d1 = other.d
        new_n = n1 * self.d + d1 * self.n
        new_d = d1 * self.d
        g = gcd(new_n, new_d)
        return Fraction(new_n // g, new_d // g)


def check_dbug(p, q):
    if p >= q:
        return False
    x = str(p / q)
    x = x[2: 10]
    if len(x) < 8:
        return False
    if x[:4] != x[4:]:
        return False
    if x[:2] == x[2:4]:
        return False
    if x[0] == x[1]:
        return False
    return True

def check_different(A, K, L, O, frac):
    frac = str(frac)
    dbug = list(map(int, frac[2:6].strip()))
    all_digits = dbug +  [A, K, L, O]
    if len(set(all_digits)) == 8:
        return True
    else:
        return False

ans = Fraction(0, 1)

for A in range(10):
    for K in range(10):
        for L in range(10):
            for O in range(10):
                if len({A, K, L, O}) < 4:
                    continue

                p = A * 101 + K * 10
                q = L * 101 + O * 10

                if check_dbug(p, q):
                    if check_different(A, K, L, O, p / q):
                        ans += Fraction(p, q)


print(ans.n, ans.d)
print(ans.n * ans.d)

# Answer is 11716
