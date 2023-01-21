dic = {}
for a in range(1, 100):
    for b in range(a, 100):
        for c in range(b, 100):
            if (a * b * c == 2450):
                sm = a + b + c
                dic[sm] = dic.get(sm, 0) + 1
                if sm == 64:
                    print(a, b, c)

print(dic)
# AGES ARE 7, 7, 50, KYLIE'S AGE: 49
print(7 ** 3 + 7 ** 3 + 49 ** 3 + 50 ** 3)

# ANSWER IS 243335
