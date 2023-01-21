import math
from math import isqrt

def is_perfect_square(p):
    if isqrt(p) ** 2 == p:
        return True
    return False


def find_solution(n):
    x = int(math.sqrt(n))
    y, z, r = x, 1, x << 1
    e1, e2 = 1, 0
    f1, f2 = 0, 1
    while True:
        y = r * z - y
        z = (n - y * y) // z
        r = (x + y) // z

        e1, e2 = e2, e1 + e2 * r
        f1, f2 = f2, f1 + f2 * r

        a, b = f2 * x + e2, f2
        if a * a - n * b * b == 1:
            return (a, b)

mx_x = 0
related_n = 0

for i in range(100001):
    if is_perfect_square(i): continue


    ans = find_solution(i)
    if ans[0] > mx_x:
        related_n = i
        mx_x = ans[0]

print(related_n, mx_x)


# ans is 92821
# runtime < 5 sec
