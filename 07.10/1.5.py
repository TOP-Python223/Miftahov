from math import *
from pprint import pprint
from random import randrange as rr

def func_mean(iterator: str | list | tuple) -> dict:
    """Вычисляет набор средних значений для итерируемого объекта"""
    nums = ()
    try:
        if isinstance(iterator, str):
            nums = tuple(float(num) for num in iterator.split())
        elif isinstance(iterator, (tuple, list)):
            nums = tuple(iterator)
        else: return None
    
        res = (['среднее арифметическое', sum(nums) / len(nums)],
            ['среднее геометрическое', pow(prod(nums), 1/len(nums))],
            ['среднее квадратичное', sqrt(1/len(nums) * sum(num**2 for num in nums))],
            ['среднее гармоническое', len(nums) / sum(1/num for num in nums)])
    
        res = dict(sorted(res, key=lambda val: val[1]))
        return res
    except TypeError:
        return None

m_str = ' '.join(str(rr(1, 99)) for _ in range(rr(5, 20)))
m_list = [float(rr(0, 40)) for _ in range(rr(6, 15))]
m_tuple = tuple(float(rr(3, 25)) for _ in range(rr(4, 30)))
    

x = func_mean(m_str)
pprint(x, sort_dicts=False)


# Ввод:
# func_mean(m_str)

# Вывод:
# {'среднее гармоническое': 33.973893529043096,
 # 'среднее геометрическое': 46.948696918779866,
 # 'среднее арифметическое': 57.785714285714285,
 # 'среднее квадратичное': 65.14873093819358}
 

 # Ввод:
# func_mean(m_list)

# Вывод:
# {'среднее гармоническое': 6.535477150465025,
 # 'среднее геометрическое': 12.539864928727019,
 # 'среднее арифметическое': 16.333333333333332,
 # 'среднее квадратичное': 18.29389697868299}


# Ввод:
# func_mean({'a': 1, 'b': 2})

# Вывод
# None




