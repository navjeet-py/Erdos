def dec_to_base(num,base):
    base_num = ""
    while num>0:
        dig = int(num%base)
        if dig<10:
            base_num += str(dig)
        else:
            base_num += chr(ord('A')+dig-10)
        num //= base
    base_num = base_num[::-1]
    return base_num

possibles = [
    [1, 2, 3, 4],
    [0, 2, 3, 4, 5],
    [0, 1, 3, 4, 5],
    [0, 1, 2, 4, 5],
    [0, 1, 2, 3, 5]
]

def check(house):
    if len(set(house)) < 5:
        return False
    for person in range(5):
        if house[person] not in possibles[person]:
            return False
    return True

cnt  = 0

for i in range(6**5):
    x = dec_to_base(i, 6)
    x = list(map(int, x.strip()))
    if (check(x)):
        cnt += 1
print(cnt)

# ANSWER IS 256.