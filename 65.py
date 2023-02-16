from sympy import expand, symbols

x = symbols('x')
gfg_exp = x * x * x + x * x +  x + 1

exp = expand(gfg_exp ** 50)
print(exp)
