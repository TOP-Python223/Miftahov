a = b = 1
n = int(input('Введите натуральное число: \n'))

for i in range(n):
    print(a, end = ' ')
    a, b = b, a + b
    
    
    
    