print('Введите два целых числа не равных нулю: ')
a = int(input())
b = int(input())

if a % b == 0:
    print(f"{a} делится на {b} нацело", f"Частное: {a//b}", sep = '\n')
else:
    print(f"{a} не делится на {b} нацело", f"Частное: {a//b}", f"Остаток: {a%b}", sep = '\n')