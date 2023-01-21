ans  = 0
for i in range(123456789, 1234567891):
    x = str(i).count('1')
    ans += x
    if i % 123456789 == 0:
        print(i)

print(ans)

# ANSWER IS 1298765422
# WROTE THE SAME CODE IN C++. RUNTIME WAS ~20 seconds.
# PYTHON IS TAKING TOO MUCH TIME.