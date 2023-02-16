

mod = 10 ** 8
a, b = 0, 1
for i in range(10 ** 10):
    if a == 1 and b == 1 and i > 10:
        print(i)
        break
    a, b = b, (a + b) % mod

"""
Ran this code in c++. Got the result in 2-3 seconds.
"""

# Answer is 150000000
