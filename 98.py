X = [1, 1]
Y = [1, 7]

for i in range(1000):
    X.append(X[-1] * 1 + X[-2] * 2)
    Y.append(Y[-1] * 2 + Y[-2] * 3)
for i in X:
    if i in Y:
        print(i)


# Answer is 15129