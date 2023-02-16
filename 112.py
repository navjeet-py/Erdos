from math import sqrt, exp, log


def nth_root(x, n):
    return exp(log(x) / n)

def f(parameters):
    root, first, second, positive = parameters
    ans = nth_root((first + second * sqrt(5)) / 2, root)
    if not positive:
        return -ans
    return ans


array = [
    [5, 11, 5, True],
    [8, 47, 21, True],
    [6, 18, 8, True],
    [16, 2207, -987, False],
    [22, 39603, -17711, False],
    [11, 199, 89, True],
    [30, 1860498, -832040, True],
    [13, 521, 233, True],
    [12, 322, -144, False],
    [10, 123, -55, False],
    [26, 271443, -121393, False]
]



string = ""
for term in array:
    root, first, second, positive = term
    if (str(second)[0] != '-'):
        second = "+" + str(second)
    if positive:
        string += '+'
    else:
        string += '-'

    x = f"(({first}{second}*sqrt(5))/2)^(1/{root})"
    string += x

print(string)

a = 3.6180339887498948482045868343656381177203091798057628621354486227
b = 2
print((a + b) * 1000000000)

""" We did not receive required accuracy using python. So, we wrote code for the command we can give to wolfram alpha"""

# ANSWER IS 5618033988
