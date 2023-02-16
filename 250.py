x = 0
d = 4.25
for i in range(20):
    x += (d / 10)
    d /= 10
print(x)


"""
I solved using a weird logic. At every position, 2,3,5,7 can be with equal probability.
so, on average, every position will have 4.25. so, put 4.25 at every position using decimal system. 
and find the recurring decimal for infinite additions, that is 0.47222...
its fraction will be 17/36.
"""
# ANSWER IS 53. p = 17, q = 36