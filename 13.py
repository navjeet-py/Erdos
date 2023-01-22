digits = [1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def is_prime(N):
    for i in range(2, N):
        if N % i == 0:
            return False
        if i * i > N:
            return True

def next_permutation(L):
    n = len(L)
    i = n - 2
    while i >= 0 and L[i] >= L[i + 1]:
        i -= 1

    if i == -1:
        return False
    j = i + 1
    while j < n and L[j] > L[i]:
        j += 1
    j -= 1
    L[i], L[j] = L[j], L[i]
    left = i + 1
    right = n - 1

    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1

    return True


for i in range(1000):
    number = ''
    for d in digits:
        number += str(d)
    number = int(number)
    if is_prime(number):
        print(number)
        break
    next_permutation(digits)

# ANSWER IS 10123457689.
