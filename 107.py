def polynomial(degree, coefficients, x):
    term = 1
    ans = 0
    for i in range(degree + 1):
        ans += (term * coefficients[i])
        term *= x
    return ans


def check(n):
    for a in range(-120, 121):
        for b in range(-24, 25):
            for c in range(-6, 7):
                for d in range(-5, 6):
                    for e in range(-2, 3):
                        for f in range(-1, 2):
                            positives = [polynomial(5, [a, b, c, d, e, f], 0),
                                         polynomial(5, [a, b, c, d, e, f], 1),
                                         polynomial(5, [a, b, c, d, e, f], 2),
                                         polynomial(5, [a, b, c, d, e, f], 5),
                                         ]
                            negatives = [polynomial(5, [a, b, c, d, e, f], -1),
                                         polynomial(5, [a, b, c, d, e, f], -2),
                                         polynomial(5, [a, b, c, d, e, f], -5),
                                         ]
                            if max(positives) == n and min(positives) == n:
                                if max(negatives) == -n and min(negatives) == -n:
                                    print(a, b, c, d, e, f)
                                    return True
    return False


#

for i in range(50):
    print(i, check(i))
