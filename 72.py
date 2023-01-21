"""
I can not come directly after G.
H can not come directly after G or B.
T can not come directly after T or U.
The string should be a palindrome.

"""

after = {
    "G": "GTUB",
    "I": "ITHUB",
    "T": "GIHB",
    "H": "ITHU",
    "U": "GIHUB",
    "B": "GITUB"
}

N = 7162534 // 2
mod = 10 ** 9 + 7

last = {}
latest = {}
for char in "GITHUB":
    last[char] = 1
#
# print("START")
#
# for i in range(2, N + 1):
#     if i % (500000) == 0:
#         print(i)
#
#     for char in "GITHUB":
#         latest[char] = 0
#         for nb in after[char]:
#             latest[char] += last[nb]
#         latest[char] %= mod
#         if char == 'B':
#             last = latest


print(latest)
print(last)
latest = {'G': 319576837, 'I': 897122273,
          'T': 915334212, 'H': 505529994,
          'U': 565547860, 'B': 395162329}

ans = 0
for key, val in latest.items():
    if key != 'T':
        ans += val
print(ans)
print(ans % mod)

# ANSWER IS

# WHERE THE FUCK AM I DOING THIS WRONG...