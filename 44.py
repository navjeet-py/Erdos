unit = pow(4128, 6, 10) + pow(6, 4128, 10)
print(unit)

# k is a multiple of 4.
# unit digit of k is 0.


ans = 0
for n in range(1, 17040385):
    x = n % 10
    if x == 5:
        ans += 5
    elif x == 0:
        ans += 0
    elif x % 2 == 0:
        ans += 6
    else:
        ans += 1
print(ans)

# ANSWER IS 56233268.