def todec_convert(num: str, 
                 *,
                 num_sys: int = 16) -> int:
    """Преобразует число из исходной системы счисления в десятичную"""
    x = 0
    for i in range(len(num)):
        if chars.index(num[i]) >= int(num_sys):
            x = f'Цифры {num[i]} нет в {num_sys}-ичной системе счисления'
            break
        else:
            x += chars.index(num[len(num) - i - 1]) * int(num_sys)**i
    return x 

def fromdec_convert(num: int,
               *,
               num_sys: int = 16) -> str:
    """Преобразует число из десятичной в целевую систему счисления"""
    y = ''
    try:
        while num > num_sys:
            y = chars[num % num_sys] + y
            num = num // num_sys
        y = chars[num % num_sys] + y
        return y
    except:
        return num

def numsys_convert(number: str,
                   in_numsys: int,
                   out_numsys: int) -> str:
    """Преобразует число из исходной в целевую систему счисления"""
    return fromdec_convert(todec_convert(number, 
                                         num_sys = in_numsys), 
                           num_sys = out_numsys)


chars = "0123456789ABCDEF"

number = input('Введите число для преобразования: ')
in_numsys = int(input('Введите исходную систему счисления: '))
out_numsys = int(input('Введите целевую систему счисления: '))

print(numsys_convert(number, in_numsys, out_numsys))


# Ввод:
# Введите число для преобразования: 1362
# Введите исходную систему счисления: 11
# Введите целевую систему счисления: 15
# Вывод:
# 7C7

# Ввод:
# Введите число для преобразования: 311010
# Введите исходную систему счисления: 2
# Введите целевую систему счисления: 11
# Вывод:
# Цифры 3 нет в 2-ичной системе счисления