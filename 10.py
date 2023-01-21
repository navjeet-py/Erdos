x, y = 1,1
ans = 0
x_increment = 2
y_increment = 4


N = 10001
for i in range(N):
    ans += x
    ans += y
    x += x_increment
    y += y_increment
    x_increment += 2
    if (i % 2 == 1): y_increment += 4

print(ans - 1)


# ans is 666916710001
# time < 1 sec