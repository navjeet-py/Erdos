for i in range(1, 1000):
    if pow(3, i, 10**4) == 1:
        print(i)
        break

"""
500 is the period.
m = n + 500
k = n + 1000
k < m + n
1000 + n < n + 500 + n
n > 500 => n = 501
perimeter = 3003
"""

# ANSWER IS 3003