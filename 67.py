S = [3, 27]

for i in range(1000):
    x = pow(3, S[-1], 1073741824)
    S.append(x)

print(S[-10:])


# ANSWER IS 1018526523.