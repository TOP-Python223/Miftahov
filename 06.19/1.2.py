#from random import randint

#n, sum_n = int(input('Введите натуральное число: ')), 0
#if n > 0:
#    for _ in range(n):
#        a = randint(-100, 100)
#        print(a)
#        if a > 0:
#            sum_n += a
#    print('\nСумму положительных чисел: ', sum_n)
   
#else:
#    print('Ошибка ввода!')
    
    
# на почти аналогичном задании 1.7 понял что не верно прочитал условие задачи, но решил оставить тут решение через функцию случайных чисел




n, sum_n = int(input('Введите натуральное число: ')), 0
if n > 0:
    for i in range(n):
        m = int(input(f'Введите {i+1} целое число: '))
        if m > 0:
            sum_n += m
    print('\nСумму положительных чисел: ', sum_n)
else:
    print('Ошибка ввода!')  

