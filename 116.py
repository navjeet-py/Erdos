from math import factorial

mp = {}
for area in range(200, 300):
    x = factorial(area)
    while x % 10 == 0:
        x //= 10

    last_5 =int(str(x)[-5:])
    mp[last_5] = mp.get(last_5, 0) + 1
print(mp)