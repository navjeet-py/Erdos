F = [0, 1]
M = [2]
mod = 10 ** 9 + 7

for i in range(1000):
    F.append((F[-1] + F[-2]) % mod)

for i in range(1, 600):
    if i % 2 == 1:
        M.append(-1)
        continue

    M.append((5 * F[i - 1] - M[i - 2]) % mod)
    if M[-1] < 0:
        M[-1] += mod

print(M[:20])
ans = 1
for i in range(1, 10):
    ans *= M[2**i]
    ans %= mod
print(ans % mod)

# ANSWER IS 754854590.