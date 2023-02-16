def power_in_factorial(base, x):
    p = x
    ans = 0
    while p <= base:
        ans += (base // p)
        p *= x
    return ans


def power_in_binomial(n, r, x):
    return power_in_factorial(n, x) - power_in_factorial(r, x) - power_in_factorial(n - r, x)


X = [
    power_in_binomial(66, 24, 3),
    power_in_binomial(73, 27, 2),
    power_in_binomial(3280, 1367, 3),
    power_in_binomial(3712, 2005, 2),
    power_in_binomial(14348, 7519, 2),
    16,
    19
]

print(X)

K = 20
#
# for a in range(-K, K):
#     for b in range(-K, K):
#         for c in range(-K, K):
#             for d in range(-K, K):
#                 S = []
#
#                 for i in range(7):
#                     S.append(a*i**3 + b*i**2 + c*i + d)
#                 # print(S)
#                 if S == X:
#                     print(S, a, b, c, d)

S = [2, 5, 7, 11, 13, 16, 19, 21, 25, 27, 30, 33, 35, 39, 41, 45, 47, 50, 53, 55, 59, 61, 64, 67, 69, 73, 75, 79, 81,
     84, 87, 89, 93, 95, 98, 101, 103, 107, 109, 112, 115, 117, 121, 123, 127, 129, 132, 135, 137, 141, 143, 146, 149,
     151, 155, 157, 161, 163, 166, 169, 171, 175, 177, 180, 183, 185, 189, 191, 194, 197]

print(S[67])
for i in range(1, len(S)):
    print(S[i] - S[i - 1], end=' ')

