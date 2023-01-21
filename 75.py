# PROBLEM STATEMENT NOT CLEAR
def is_prime(N):
    if N == 2:
        return True
    for i in range(2, N):
        if i * i > N:
            return True
        if N % i == 0:
            return False

prime = [False for i in range(10**5)]

for i in range(2, 10**5):
    prime[i] = is_prime(i)
print(" PRIME LIST DONE")
# print(list(enumerate(prime[:20])))

def check(x):
    ls = []
    for i in range(5):
        ls.append(int(x[i]))
        for j in range(i + 1, 5):
            ls.append(int(x[i] + x[j]))
            for k in range(j + 1, 5):
                ls.append(int(x[i] + x[j] + x[k]))
                for l in range(k + 1, 5):
                    ls.append(int(x[i] + x[j] + x[k] + x[l]))
    # print(ls)
    for num in ls:
        if prime[num]:
            return False
    return True


# check('78956')

cnt = 0
for i in range(10**4, 10**5):
    if i % (10**4) == 0:
        print(i)
    if check(str(i)):
        cnt += 1

print(cnt)