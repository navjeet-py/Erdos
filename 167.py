pks = [(7, 5), (5, 3)] # FOUND OUT USING NUMBER THEORY CONCEPTS. Using formula of sum of divisors.
ans = 0
for pk in pks:
    p, k = pk
    n = 2 ** k * 3 * p
    ans += n
print(ans)

# ANSWER IS 792.