from typing import Callable

def myround(func_obj: Callable, 
            *args: int | float, 
            logic_key: bool = True) -> str | float:
    """Возвращает округленное до двух знаков после запятой значение типа str или float"""
    res = func_obj(*args)
    return f"{res:.2f}" if logic_key else float(f"{res:.2f}")
    
print(myround(lambda k, x, b: k * x + b, 2, 4, 6, logic_key = True))
# 14.00    

print(myround(lambda a, b, c, x: a * x**2 + b * x + c, 5.4, 15.3, 7.7, 2.6, logic_key = False))
# 83.98


