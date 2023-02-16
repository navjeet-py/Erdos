def is_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
        if i * i > x:
            return True

ones = 0
threes = 0

for i in range(3, 1000000, 2):
    if is_prime(i):
        if i % 4 == 1:
            ones += 1
        else:
            threes += 1
print(ones, threes)
