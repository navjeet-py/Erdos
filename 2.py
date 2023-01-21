def rhs(x):
    return x ** 6 + 8 * x ** 4 - 6 * x ** 2 + 8


def find_closest_x(y):
    lhs = y ** 6
    left, right = 0, 1000
    counter = 0
    closest = 0
    while counter < 50:
        mid = (left + right) / 2
        if rhs(mid) > lhs:
            right = mid
        else:
            left = mid
        counter += 1
    print(left, right)



find_closest_x(1)
