def determinantOfMatrix(mat, n):
    temp = [0] * n
    total = 1
    det = 1
    for i in range(0, n):
        index = i
        while (index < n and mat[index][i] == 0):
            index += 1
        if (index == n):
            continue
        if (index != i):
            for j in range(0, n):
                mat[index][j], mat[i][j] = mat[i][j], mat[index][j]
            det = det * int(pow(-1, index - i))
        for j in range(0, n):
            temp[j] = mat[i][j]
        for j in range(i + 1, n):
            num1 = temp[i]
            num2 = mat[j][i]

            for k in range(0, n):

                mat[j][k] = (num1 * mat[j][k]) - (num2 * temp[k])

            total = total * num1
    for i in range(0, n):
        det = det * mat[i][i]

    return int(det / total)


for N in range(3, 20, 2):
    mtx = []
    for i in range(N):
        row = []
        for j in range(N):
            row.append(abs(i - j))
        mtx.append(row)

    det = determinantOfMatrix(mtx, N)


    print(f"{N} => {det // (N - 1)}")


"""
We can see a pattern, that f(n) = (n-1)*(2^(n-2))
"""
mod = 10**9 + 7
N = 12345
print((pow(2, N - 2, mod) * (N - 1)) % mod)

# ANSWER IS 702313234.