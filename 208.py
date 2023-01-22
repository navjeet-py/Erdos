"""
They should have clarified question in a better way.
They mean it for n < 100 only.
"""

cnt = 0

for i in range(1, 100):
    if pow(i, i, 100) == i:
        cnt += 1
print(cnt)

# ANSWER IS 21