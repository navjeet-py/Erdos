def d(n):
    if n % 4 == 0 or n % 4 == 3:
        return 0
    if n % 4 == 1:
        return 1
    if n == 2:
        return 3
    else:
        return 1


N = 19216812112
single = N // 4
ans = single * 2
print(ans)

# ans = 9608406056
# runtime < 1 sec