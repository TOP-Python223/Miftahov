numerus_raqm = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}

def numerus_to_raqm(numerus):
    """Рекурсивная функция, переводящая римскую запись чисел в десятичную."""
    raqm = 0
    
    if len(numerus) > 1:
        num1 = numerus_raqm[numerus[0]]
        num2 = numerus_raqm[numerus[1]]
        if num1 >= num2:
            raqm += num1 + numerus_to_raqm(numerus[1:])
        else:
            raqm += num2 - num1 + numerus_to_raqm(numerus[2:])
        return raqm
        
    elif len(numerus) == 1:
        raqm += numerus_raqm[numerus]
        return raqm
    
    else:
        return raqm


while rome_num:= input('Введите римское число: '):
    print(f"{rome_num} = {numerus_to_raqm(rome_num)}")


# stdin:
# Введите римское число: XCIX
# stdout:
# XCIX = 99

# stdin:
# Введите римское число: MCMLXVI
# stdout:
# XCIX = 1966

# stdin:
# Введите римское число: CMLXV
# stdout:
# XCIX = 965

# stdin:
# Введите римское число: MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMCCCLXV
# stdout:
# MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMCCCLXV = 201365