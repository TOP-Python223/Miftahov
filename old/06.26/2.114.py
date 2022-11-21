l = []
while n := input('Введите число: '):
    l.append(int(n))
print(*[num for num in l if num < 0], sep='\n')
print(*[num for num in l if num == 0], sep='\n')
print(*[num for num in l if num > 0], sep='\n')