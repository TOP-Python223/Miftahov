from math import *
from pprint import pprint
from random import randrange as rr

def averages(arg: str | list | tuple | int | float, *args: int | float ) -> dict:
    """Вычисляет набор средних значений для итерируемого объекта, либо для произвольного количества объектов int и/или float"""
    args = (arg,) + args
    nums = ()
    
    if len(args) > 1:
        for a in args:
            if isinstance(a, (int, float)):
                nums += (a,)
            else:
                raise ValueError(f" Некорректный тип данных: \'{a}\' ")
    
    elif len(args) == 1:
        if isinstance(arg, str):
            for num in arg.split():
                try:
                    nums += (float(num),)
                except:
                    raise ValueError(f" Некорректный тип данных: \'{num}\' ")
        
        elif isinstance(arg, (tuple, list)):
            nums = tuple(arg)
            
    else:
        return "Значение не передано"
        
    
    res = (['среднее арифметическое', sum(nums) / len(nums)],
           ['среднее геометрическое', pow(prod(nums), 1/len(nums))],
           ['среднее квадратичное', sqrt(1/len(nums) * sum(num**2 for num in nums))],
           ['среднее гармоническое', len(nums) / sum(1/num for num in nums)])
    
    res = dict(sorted(res, key=lambda val: val[1]))
    return res


m_str = ' '.join(str(rr(1, 99)) for _ in range(rr(5, 20)))
m_list = [float(rr(1, 40)) for _ in range(rr(6, 15))]
m_tuple = tuple(float(rr(3, 25)) for _ in range(rr(4, 30)))
    

# stdint
pprint(averages([1, 2, 3, 4.23]), sort_dicts=False)
# Изменил '0 2 0.12 1' на '1 2 0.12 1', т.к. на 0 делить нельзя
pprint(averages('1 2 0.12 1'), sort_dicts=False)
pprint(averages(-1, 1.5, -2, 2.5), sort_dicts=False)
pprint(averages('0b010 0b110'), sort_dicts=False)
pprint(averages(1, 2, '3 4'), sort_dicts=False)
pprint(averages([1, 2], '3 4'), sort_dicts=False)

# stdout
# {'среднее гармоническое': 1.9326099371787548,
 # 'среднее геометрическое': 2.244517027586113,
 # 'среднее арифметическое': 2.5575,
 # 'среднее квадратичное': 2.823689961734468}
# {'среднее гармоническое': 0.3692307692307692,
 # 'среднее геометрическое': 0.6999271023161167,
 # 'среднее арифметическое': 1.03,
 # 'среднее квадратичное': 1.2262136844775466}
# {'среднее гармоническое': -9.23076923076923,
 # 'среднее арифметическое': 0.25,
 # 'среднее геометрическое': 1.6548754598234365,
 # 'среднее квадратичное': 1.8371173070873836}

# Traceback (most recent call last):
  # File "C:\Users\aynur\Desktop\Айнур Учёба\Занятия Геннадий\Homeworks\Miftahov\old\07.10\2.4.py", line 21, in averages
    # nums += (float(num),)
# ValueError: could not convert string to float: '0b010'

# During handling of the above exception, another exception occurred:

# Traceback (most recent call last):
  # File "C:\Users\aynur\Desktop\Айнур Учёба\Занятия Геннадий\Homeworks\Miftahov\old\07.10\2.4.py", line 51, in <module>
    # pprint(averages('0b010 0b110'), sort_dicts=False)
  # File "C:\Users\aynur\Desktop\Айнур Учёба\Занятия Геннадий\Homeworks\Miftahov\old\07.10\2.4.py", line 23, in averages
    # raise ValueError(f" Некорректный тип данных: \'{num}\' ")
# ValueError:  Некорректный тип данных: '0b010'

# Traceback (most recent call last):
  # File "C:\Users\aynur\Desktop\Айнур Учёба\Занятия Геннадий\Homeworks\Miftahov\old\07.10\2.4.py", line 52, in <module>
    # pprint(averages(1, 2, '3 4'), sort_dicts=False)
  # File "C:\Users\aynur\Desktop\Айнур Учёба\Занятия Геннадий\Homeworks\Miftahov\old\07.10\2.4.py", line 15, in averages
    # raise ValueError(f" Некорректный тип данных: \'{a}\' ")
# ValueError:  Некорректный тип данных: '3 4'

# Traceback (most recent call last):
  # File "C:\Users\aynur\Desktop\Айнур Учёба\Занятия Геннадий\Homeworks\Miftahov\old\07.10\2.4.py", line 53, in <module>
    # pprint(averages([1, 2], '3 4'), sort_dicts=False)
  # File "C:\Users\aynur\Desktop\Айнур Учёба\Занятия Геннадий\Homeworks\Miftahov\old\07.10\2.4.py", line 15, in averages
    # raise ValueError(f" Некорректный тип данных: \'{a}\' ")
# ValueError:  Некорректный тип данных: '[1, 2]'





