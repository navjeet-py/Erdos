from sympy.ntheory.factor_ import totient


def f(x, n):
    ans = 0
    for i in range(1, n + 1):
        ans += pow(x, pow(2, i))
    return ans


print(totient(10**9 + 6))

