from time import sleep
from typing import Callable


def callback(func: Callable):
    """Dызвана функцию повторно через 5 секунд, если вызов оборачиваемой функции прекращается с исключением"""
    def wrapped(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
            return res
        except Exception as ex:
            print(F'Ошибка!!! {ex}\n')
            sleep(5)
            wrapped(*args, **kwargs)
    return wrapped

@callback
def my_func(a: int, b: int) -> float:
    """Возвращает частное чисел"""
    res = a / b
    return res


print(my_func(10, 0))

# stdin:
# print(my_func(10, 'a'))

# stdout:
# Ошибка!!! unsupported operand type(s) for /: 'int' and 'str'

# Ошибка!!! unsupported operand type(s) for /: 'int' and 'str'

# Ошибка!!! unsupported operand type(s) for /: 'int' and 'str'

# Ошибка!!! unsupported operand type(s) for /: 'int' and 'str'



# stdin:
# print(my_func(10, 0))

# stdout:
# Ошибка!!! division by zero

# Ошибка!!! division by zero

# Ошибка!!! division by zero

# Ошибка!!! division by zero