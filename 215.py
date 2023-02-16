"""
a = 0 (mod 500000003)
a = 1000000006 (mod 1000000007)

we need to find a (mod 1000000007 * 500000003)

"""

for a in range(10**8):
    x = a * 500000003
    if x % 1000000007 == 1000000006:
        print(x)
        break

# ANSWER IS 1000000006.