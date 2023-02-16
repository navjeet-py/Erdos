from bisect import bisect

def prime_sieve(n):
    """
    Efficient prime sieve, due to Robert William Hanks.
    Source: http://stackoverflow.com/a/2068548
    """
    sieve = [True] * (n//2)
    print('1')
    for i in range(3,int(n**0.5)+1,2):
        print(i)
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1,n//2) if sieve[i]]

"""
Limit controls the number of primes that are sieved
to cache small values of pi(x).  Wthout caching,
runtime will be exponential.
When computing pi(x), limit should be
at least sqrt(x).  A higher value of limit
that caches more values can sometimes improve performance.
"""

limit = 10**9
primes = prime_sieve(limit)

def sum_of_digit(x):
    return sum(map(int, list(str(x).strip())))

ans = 0
for x in primes:
    ans += sum_of_digit(x)
print(ans)

# RUNS IN <3 minutes
# ANSWER IS 2076414728
