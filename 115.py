mx = 0
for N in range(1, 50):
    x = 42 / N
    product = x ** N

    mx = max(mx, product)
    print(mx)

print(mx)

# ANSWER IS 5097655.