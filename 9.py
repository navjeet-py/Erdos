import math

mx = 2494800

def count_divisor(n):
    cnt = 0
    for i in range(1, (int)(math.sqrt(n)) + 1):
        if (n % i == 0):
            if (i * i == n):
                cnt = cnt + 1
            else:
                cnt = cnt + 2

    return cnt

for i in range(1, mx+1):
    if count_divisor(i) >= 300:
        print(i)
        break
    if i % (mx // 100) == 0: print(str(i // (mx // 100)) + "% done")


# ans is 2162160
# runtime < 3 minutes