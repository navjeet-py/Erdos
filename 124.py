from sympy.ntheory.factor_ import totient

def euler_phi(N):
    return int(totient(N))

N = 10**6

S = [0] * N
# S[1] = 1

for i in range(1, N):
    print(str(i) + "\n" if i % 10**5 == 0 else '', end='')
    fac = 1
    phi = euler_phi(i)
    while i * fac < N:
        S[i * fac] += phi
        fac += 1
# print(S)
print()

# We find that S(N) = N - 1

def F(N):
    ans = 0
    for i in range(1, N + 1):
        ans += S[i]
    return ans

print(F(999999) + F(888888))

# ANSWER IS 895060882716.


