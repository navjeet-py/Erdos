from math import gcd

N = 20
g = -1
for x_1 in range(1, N):
    for x_2 in range(1, N):
        for x_3 in range(1, N):
            for x_4 in range(1, N):
                for x_5 in range(1, N):
                    for x_6 in range(1, 3*N):
                        if x_1 ** 2 + x_2 ** 2 + x_3 ** 2 + x_4 ** 2 + x_5 ** 2 == x_6**2:
                            p = x_1 * x_2 * x_3 * x_4 * x_5 * x_6
                            if g == -1:
                                g = p
                            else:
                                g = gcd(p, g)

print(g)

# ANSWER IS 24
