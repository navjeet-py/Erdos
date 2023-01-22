"""

2^6 = 1 (mod 9)

"""
for n in range(1, 10):
    x = pow(2, n, 6)
    rem = pow(2, x, 9) + 1
    rem %= 9
    print(f"G({n})", rem)

ans = 13 * (999999999999 // 2) + 5

print(ans)

# ANSWER IS 6499999999992.
