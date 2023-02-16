N = 127
arr = []
total = 0
for i in range(N):
    for j in range(N):
        for k in range(N):
            for l in range(N):
                total += 1
                if (total % 10**7 == 0):
                    print(total)
                x = i / N + j / (N * N) + k / (N ** 3) + l / (N ** 4)
                arr.append(x)
arr.sort()
ans = arr[20212020]
print(ans * (10**7))

# CODE RUNS IN < 2 minutes.
# ANSWER IS 776953.


