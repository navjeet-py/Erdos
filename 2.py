for x in range(1000):
    for y_square in range(1000):
        if x * y_square == 0: continue
        if y_square ** 3 == x ** 6 + 8 * x ** 4 - 6 * x ** 2 + 8:
            print(3345 * x + 4321 * y_square)


# ANSWER IS 57566