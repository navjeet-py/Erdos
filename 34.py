def is_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def add(dic, x):
    for i in range(2, x + 1):
        if is_prime(i):
            while x % i == 0:
                dic[i] = dic.get(i, 0) + 1
                x //= i


fac = {}
for i in range(2, 101):
    add(fac, i)

ans = 1
for key, val in fac.items():
    if key != 2:
        ans *= (val + 1)

print((ans % (10 ** 9 + 9)) - 1)

# ANSWER IS 943938260

