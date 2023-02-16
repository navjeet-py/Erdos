mtx = [
    [8, 8, 4],
    [1, 1, 8],
    [4, 4, 1]
]
ans = 0
for i in range(3):
    for j in range(3):
        ans += (mtx[i][j] * (i + j + 2))

print(ans)

# ANSWER IS 145