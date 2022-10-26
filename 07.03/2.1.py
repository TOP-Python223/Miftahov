from random import randrange as rr

l1 = set([rr(1, 20) for _ in range(rr(8, 12))])
l2 = set([rr(1, 20) for _ in range(rr(8, 12))])

print(list(l1), list(l2), sep='\n', end='\n\n')

n1, n2 = l1 - l2, l2 - l1
l1, l2 = list(n1), list(n2)

print(l1, l2, sep='\n')