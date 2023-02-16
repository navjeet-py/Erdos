# string = "1"
#
# n = 4
# for i in range(n, 0, -1):
#     new = f"sum({string}) for a{i}=a{i-1} to n"
#     string = new
#
# print(string)
#
# X = [26,351, 3276, 23751, 142506,736281, 3365856]
# """
# n
# n(n+1)/2
# n(n+1)(2n+1)/6
# """
# print((26*27)//2)
# print((26*27 * 53)//)


def f(count, n):
    ans = 1
    for i in range(count):
        ans *= (n + i)
        ans //= (i + 1)
    return ans
print(f(25, 26))

# ANSWER IS 126410606437752.