from random import randrange as rr, choice
from string import digits

# Исользовал позиционно-ключевые параметры, т.к. аргументы неоднотипные 
def del_MinMax(num_list: list[int],
               n: int,
               change_num_list: bool,
               /) -> list:
    """Удаляет n минимальных и n максимальных значений из списка чисел"""
    if len(num_list) // 2 <= n:
        return 'Число n некорректно'
    if change_num_list:
        num_list.sort()
        num_list = num_list[n: -n]
        return None
    else:
        num_list_copy = num_list.copy()
        num_list_copy.sort()
        num_list_copy = num_list_copy[n: -n]
        return num_list_copy


m_list = []
for _ in range(rr(2, 20)):
    num = []
    for _ in range(rr(2, 4)):
        num += [choice(digits)]
    m_list += [int(''.join(num))]

m_n = int(rr(1, 9))

m_bool = choice([True, False])

print(f"{m_list = }\n{m_n = }\n{m_bool = }\n")
print(del_MinMax(m_list, m_n, m_bool))

# stdout
# m_list = [98, 340, 436, 84, 19, 456, 7, 15, 96, 50, 591, 447, 7, 547, 673, 349, 825]
# m_n = 5
# m_bool = False

# [84, 96, 98, 340, 349, 436, 447]

# stdout
# m_list = [900, 81, 88, 42, 34, 43, 43, 59, 13]
# m_n = 8
# m_bool = False

# Число n некорректно

# stdout
# m_list = [49, 764, 85, 38, 50, 12, 522, 355, 42, 23, 595, 352, 62, 22, 17, 767, 437, 51]
# m_n = 8
# m_bool = True

# None


    
