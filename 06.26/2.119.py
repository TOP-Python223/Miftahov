l = []
while n := input('Введите число: '):
    l.append(int(n))
l.sort()
mean_v = sum(l) // len(l)
print(f'Среднее значение введенного ряда чисел = {mean_v}\n\n')
print('Список чисел ниже среднего:', [num for num in l if num < mean_v], sep='\n', end='\n\n')
print('Список чисел равно среднему:', [num for num in l if num == mean_v], sep='\n', end='\n\n')
print('Список чисел выше среднего:', [num for num in l if num > mean_v], sep='\n')


