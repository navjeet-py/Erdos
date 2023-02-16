"""
gcd(2^a-1, 2^b-1) = 2^gcd(a,b) - 1

"""
from math import gcd

print(pow(2, gcd(10**10, 8**8), 1000000007))

# ANSWER IS 812734592.