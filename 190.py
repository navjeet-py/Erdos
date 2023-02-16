def is_prime(n):
    if n == 2:
        return True
    for i in range(2, n):
        if i * i > n:
            return True
        if n % i == 0:
            return False


N = 10**7

primes = []
primes_till = [0] * (N + 1)

for i in range(2, (N + 1) // 2 + 2):
    primes_till[i] = primes_till[i - 1]
    if is_prime(i):
        primes.append(i)
        primes_till[i] = primes_till[i - 1] + i
    print(f"{i} " if i % 1000000 == 0 else '', end='')
# for i in range((N + 1) // 2, N + 1):
#     primes_till[i] = primes_till[i - 1]

# print(primes)
# print(primes_till)

ans = 0

for prime in primes:
    take_till = N // prime
    ans += (primes_till[take_till] * prime)
    if prime * prime < N:
        ans += (prime * prime)

print()
print(ans // 2)

# ANSWER IS 9322298311255.

