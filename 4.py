
def check(n):
    b = bin(n)[2:]
    h = hex(n)[2:]
    o = oct(n)[2:]
    if b == b[-1::-1] and o == o[-1::-1] and h == h[-1::-1]:
        return True
    return False


def solve_noob():
    sm = 0
    for i in range(1, 10 ** 9):
        if i % 10000000 == 0: print(str(i // 10000000) + "% done")
        if check(i):
            sm += i
    print(sm)


# solve_noob()

def pro():
    sm = 0
    for i in range(200000):
        b = bin(i)[2:]
        first = int(b + b[-1::-1], 2)
        second = int(b + '0' + b[-1::-1], 2)
        third = int(b + '1' + b[-1::-1], 2)
        if first <= 10 ** 9 and check(first):
            sm += first
        if second <= 10 ** 9 and check(second):
            sm += second
        if third <= 10 ** 9 and check(third):
            sm += third
    print(sm)


pro()

# ans is 2124805299
# runtime < 3 sec