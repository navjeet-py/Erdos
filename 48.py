F = [1, 1]

mod = 10 ** 8

st = set()

for i in range(10 ** 8):
    x = F[-1] + F[-2]
    if x in st:
        print(x, i)
    st.add(x)

    if i % (10 ** 7) == 0:
        print(i)
    F.append((F[-1] + F[-2]) % mod)

print('DONE')
