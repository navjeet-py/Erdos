"""
All non-perfect squares have even factors, so they will flip even times,
while all perfect squares will flip odd times, and finally will be down.
So, all we need to find is total number of perfect squares till N.
"""
import math

N = 12345678987654321
print(N - int(math.sqrt(N)))

# ANSWER IS 12345678876543210.
