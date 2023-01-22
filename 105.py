ls = [0, 2]
for i in range(2, 65540):
    ls.append(ls[-1] + i)
print(ls[:10])
print(ls[65536])

# ANSWER IS 2147516417