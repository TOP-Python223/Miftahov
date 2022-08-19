m = int(input('Введите целое число #1: '))
n = int(input('Введите целое число #2: '))

if m <= n:
    for i in range(m, n+1):
        print(i, end = ' ')

