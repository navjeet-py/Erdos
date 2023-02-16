"""
 6x^2−5mx+m^2=0
 D = 25m^2 - 24m^2 = m^2
 roots = (5m +- m)/12

"""

cnt = 0
for m in range(1, 1001):
    if (4 * m) % 12 == 0 or (6 * m) % 12 == 0:
        cnt += 1
print(cnt)


# ANSWER IS 667