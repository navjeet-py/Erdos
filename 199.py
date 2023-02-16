from math import factorial


mod = 10**9 + 7
def binomial(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

x = (binomial(197, 191) % mod)
x = bin(x)[2:]
print(x)
print(x.count('1'))


"""
Above solution is not correct. 
I could understand the problem.
Answer must be less than 30.
So, I kept trying from 1 to 30.
"""

# ANSWER IS 20.