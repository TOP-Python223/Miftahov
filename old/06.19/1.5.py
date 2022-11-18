print('Введите число, кратное 7-ми: ')
m = []
while True:
    n = int(input())
    m += [n]
    if n % 7 != 0: break
print(*m)
   
    