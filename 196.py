from math import gcd

total = 0
win = 0

for a in range(4):
    for b in range(4):
        for c in range(4):
            for d in range(4):
                if a + b + c + d == 3:
                    total += 3
                    if a >= b:
                        win += 1
                    if a >= c:
                        win += 1
                    if a >= d:
                        win += 1



g = gcd(win, total)
win //= g
total //= g
print(pow(win, total, 10 ** 9 + 7))

# ANSWER IS 53945879.
