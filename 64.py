import numpy

for m in range(1, 10):
    x_list = [i for i in range(3 * m + 1)]
    y_list = [2, 1, 0] * m + [2]
    fit = numpy.polyfit(x_list, y_list, deg=3*m)
    alpha = list(map(float, fit))
    value_3m_plus_1 = 0
    x = 3 * m + 1
    curr = 1
    for i in range(3 * m, -1, -1):
        value_3m_plus_1 += (curr * alpha[i])
        curr *= x
    print(m, value_3m_plus_1)


# ANSWER IS 5