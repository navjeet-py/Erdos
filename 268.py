N = 1234567
average = (N + 1) // 2

total = 0
for first in range(1, N + 1):
    total += first
    total += (average * first)
print(total // N)

# ANSWER IS 381040153940
