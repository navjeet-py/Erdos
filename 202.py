N = 10**18

x = N // 6

counts = [
    x,
    x + 1,
    x + 1,
    x + 1,
    x + 1,
    x
]

print(list(enumerate(counts)))

rem = 5
for i in range(10):
    print(pow(5, 6*i+rem, 10**rem))

ans = 0

ans += (5 * counts[1])
ans += (25 * counts[2])
ans += (125 * counts[3])
ans += (3125 * (counts[4] - 1))
ans += 625
ans += (40625 * (counts[5] - 2))
ans += (3125 + 28125)

print(ans % (10**9 + 7))
