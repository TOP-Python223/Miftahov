from fractions import Fraction as F
from math import lcm

def make_line(x):
    """"""
    x_lcm = 2 * (lcm(*[n.denominator for n in x]))
    line = ''
    i_frac = 0
    for i in range(1, x_lcm):
        if i == x_lcm * x[i_frac]:
            line += '|'
            if i_frac < len(x) - 1:
                i_frac += 1
        else:
            line += '—'
    line = '|' + line + '|'
    return line

def func(r):
    """"""
    top = labbel = ' ' * (len(r) + 1)
    t_n = [0] + t_sorted + [1]
    i_frac = 0
    for i in range(len(r)):
        d = str(t_n[i_frac])
        if r[i] == '|':
            if i_frac % 2 != 0:
                top = top[:i - (len(d) // 2)] + d + top[i + len(d):]
            else:
                labbel = labbel[:i - (len(d) // 2)] + d + labbel[i + len(d):]
            i_frac += 1
    print(top)
    print(r)
    print(labbel)
    

t = list((F(1, 2), F(1, 3), F(1, 4)))
t_sorted = sorted(t)
print(t_sorted, '\n\n')
r = make_line(t_sorted)

func(r)
