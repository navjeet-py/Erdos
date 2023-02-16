from math import gcd

gcd_sum = 0
cnt = 0

for i in range(1, 2020):
    for j in range(1, 2020):
        if i == j: continue
        cnt += 1
        gcd_sum += gcd(i, j)
print((gcd_sum / cnt) * 1000)

# ANSWER IS 4374
