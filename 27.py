import math


def is_prime(x):
    for i in range(2, x + 1):
        if i * i > x:
            return True
        if x % i == 0:
            return False


# for x in range(9, 10000000, 10):
#     if is_prime(x):
#         cnt = 0
#         for pp in range(11):
#             nxt = x * 3 + 2
#             if is_prime(nxt):
#                 cnt += 2
#         if cnt == 11:
#             print(x)
N = 10 ** 10
print((math.sqrt(N) - math.sqrt(N - 1)) * 10 * 13)


def check(x):
    cnt = 0
    for pp in range(11):
        x = x * 3 + 2
        if is_prime(x):
            cnt += 1
    if cnt == 11:
        return True
    else:
        return False

while True:
    x = int(input())
    if (check(x)):
        print(x, check(x))
    else:
        print('-', end=' ')

