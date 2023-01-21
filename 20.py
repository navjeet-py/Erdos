count  = 0
for i in range(2**20):
    x = bin(i)[2:]
    x = '0' * (20 - len(x)) + x
    number = ''
    for i in range(20):
        if x[i] == '1':
            number += '7'
        else:
            number += '5'
    number = int(number)
    if number % 35 == 0:
        count += 1

print(count)

# answer is 74898