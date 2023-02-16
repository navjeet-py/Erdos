"""

eg. for N = 12
1 <--> 2 <--> 4  <--> 8
3  <--> 6  <--> 12
5  <--> 10
7
9
11

for every odd number, a new graph will start.
ans = 0
for every odd x, ans += (floor(log(N/x)) + 1) + 1 / 2

"""

from math import log2

N = 4444444444
ans = 0
for odd in range(1, N, 2):
    x = int(log2(N / odd)) + 1
    ans += (x // 2)
    if (x % 2 == 1): ans += 1
print(ans)

""" Ran this code in C++, in approx 10 seconds."""

# ANSWER IS 2962962963