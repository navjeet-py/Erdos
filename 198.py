# N = 10
for N in range(5, 40):
    ans = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            ans += (i ^ j)
    print(ans % N, N)
