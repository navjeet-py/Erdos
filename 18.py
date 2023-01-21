import random

def one_game():
    varun = 1
    sandeep = 2
    for i in range(10):
        x = random.randrange(4)
        if x < 3:
            varun += 1
        else:
            sandeep += 1

        if varun == 5:
            return 'V'
        if sandeep == 5:
            return 'S'


varun = 0
sandeep = 0
for i in range(10 ** 6):
    winner = one_game()
    if winner == 'V':
        varun += 1
    else:
        sandeep += 1

varun_winning = int((varun / (varun + sandeep)) * 2000)
sandeep_winning = 2000 - varun_winning

print(pow(varun_winning, sandeep_winning, 10**9+7))

# answer is 440052480