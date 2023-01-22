ans = 0

for i in range(2**7):
    x = bin(i)[2:]
    x = '0' * (7 - len(x)) + x
    x = x.replace('0', '3')
    x = x.replace('1', '7')
    x = int(x)
    if x % 10 == 3 and x % 7 == 0:
        ans += x

print(ans)

# ANSWER IS 52177797.