from sympy.ntheory.factor_ import totient

x = int(totient(2097152))
print(x)
for i in range(1, x):
    if pow(201413, i, 2097152) == 1:
        print(i)
        break

# answer is 524288.