l = []
while n := input('Введите число: '):
    l.append(int(n))
if len(l) < 4:
    print('Вы ввели менее 4-х чисел')
else:
    print(l)
    l.sort()
    print(l[1: -1])

