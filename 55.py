from math import sqrt

format = "6_6_6_0_0_6_6_6_0_0"
# print(format.count("_"))
# x = x.replace('_', '9')
# x = int(x)
#
# print(x, sqrt(x))
#
# x = str(x).replace('9', '0')
# x = int(x)
#
# print(x, sqrt(x))

for i in range(2461828590, 2640017217, 10):

    x = i * i
    p = str(x)
    cnt = 0
    for idx in range(0, 19, 2):
        if p[idx] == format[idx]:
            cnt += 1
        else:
            break
    if cnt == 10:
        print(i)
        break

# ANSWER IS 2503521600.