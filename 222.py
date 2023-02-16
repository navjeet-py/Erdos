from math import gcd
N = 10**6
pairs_count = 0
total = (N * (N - 1)) // 2

for i in range(1, N+1):
    pairs_count += (N // i - 1)

g = gcd(pairs_count, total)
total //= g
pairs_count //= g
print(pairs_count, total, pairs_count + total)


# ANSWER IS 3246834221
