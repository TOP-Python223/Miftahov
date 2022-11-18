n = int(input('\nВведите натуральное число: '))
sum = 0
for i in range(1, n):
    if n % i == 0:
        sum += i
print(f'\nСумма всех делителй числа {n} составляет {sum + n}')