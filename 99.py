div, total = 0, 0

for number in range(10**4, 10**5):
    sum_of_digits = sum([int(i) for i in str(number)])
    if sum_of_digits == 41:
        total += 1
        if number % 11 == 0:
            div += 1

print(div, total)
# p/q = 6 / 35

# ANSWER IS 29.