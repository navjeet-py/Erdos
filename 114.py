N = 49770435560715869
P =  223092870

problem_from = (N // P) * P
print(problem_from)
print(N - problem_from)

sign = False

ans = 0
x = 1
for i in range(N, problem_from - 1, -1):
    if (i % 10**7 == 0): print(i)
    if (sign):
        ans += x
        sign = False
    else:
        ans -= x
        sign = True
    x *= i
    x %= P
    ans %= P
print(ans)

# ANSWER IS 210286196. RUNS IN LESS THAN 2 MINUTES.