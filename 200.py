X = 20


def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]


# for number in range(1000):
#     for i in range(2, X):
#         for j in range(i + 1, X):
#             if numberToBase(number, i) == numberToBase(number, j):
#                 print(number, i, j)

def F(i, j):
    # 1 + 2 + 3 + ... + min(i, j) - 1
    x = min(i, j)
    return (x * (x - 1)) // 2


# N = 10 ** 18
# ans = 0
# for i in range(2, N + 1):
#     ans += (((i * (i - 1)) // 2) * (N - i))

#did the above calculation using WolframAlpha.
print(41666666666666666583333333333333333291666666666666666750000000000000000 % 22011663)

# answer is 5314509.
