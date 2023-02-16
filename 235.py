def is_prime(N):
    if N == 2: return True
    for x in range(2, N):
        if x * x > N:
            return True
        if N % x == 0:
            return False

def smallest_prime_divisor(N):
    if is_prime(N): return N
    for i in range(2, N + 1):
        if N % i == 0:
            return i

ans = 15121

for i in range(2, 15121):
    ans += smallest_prime_divisor(i)

print(ans)

# KEY IDEA: (p-1)! is congruent to -1 mod p, if p is prime. Wilson's theorem.
# ANSWER IS 12560532.
