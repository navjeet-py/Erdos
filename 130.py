from math import gcd

n = 112358

numerator = (3*(n+1)*(n+2) - 2*(n+2) -2*(n+1)) ** 2
denominator = (2*(2*(n+1)*(n+2))) ** 2


g  =gcd(numerator, denominator)
numerator //= g
denominator //= g
print(numerator* denominator)

# ANSWER IS 228618086507850699690277616143553206022400.