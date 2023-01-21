from math import factorial
for i in range(10**5, (10**6) // 6):
    x = 6 * i
    reverse = (i // 1000) + (i % 1000) * 1000
    # print(i, reverse)
    if reverse == x:
        print(x)


print(factorial(27) % 1000000007)


#ANSWER IS 394134213