while n := input('Введите число и через пробел основание системы счисления: ').split():
    x = 0
    for i in range(len(n[0])):
        if int(n[0][i]) >= int(n[1]):
            x = f'Цифры {n[0][i]} нет в {n[1]}-ичной системе счисления'
            break
        else:
            x += int(n[0][len(n[0]) - i - 1]) * int(n[1])**i
    print(x)
    
print('Завершение работы программы')