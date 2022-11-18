n, sum_n = int(input('Введите натуральное число: ')), 0
if n > 0:
    for i in range(n):
        m = int(input(f'Введите {i+1} целое число: '))
        sum_n += m
    print('\nСумму чисел: ', sum_n)
else:
    print('Ошибка ввода!')   
