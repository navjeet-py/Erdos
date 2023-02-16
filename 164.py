"""
 X=100!
X^9449771607341027425 = Y mod 9449771616229914661
Z=Y  mod 1000000008
"""

from math import factorial

x = factorial(100) % 9449771616229914661
y = pow(x, 9449771607341027425, 9449771616229914661)
print("Z =", y % 1000000008)

# ANSWER IS 930562883.