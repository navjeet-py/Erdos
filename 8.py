N = 10 ** 9

prime = [True for i in range(N + 1)]

def sm_of_digit(n):
    return sum(list(map(int, str(n).strip())))

def sieve(n):
    p = 2
    while (p * p <= n):

        if (prime[p] == True):

            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
        # if p < 1000 :
        #     print(p)


print("SIEVE START")
sieve(N)
print("SIEVE DONE")


sm = 0
for i in range(10**9):
    if i % 10000000 == 0: print(str(i // 10000000) + "% done")

    if prime[i]:
        sm += sm_of_digit(i)
print(sm)



# print(sm_of_digit(19834))
# print(sm_of_digit(341003))