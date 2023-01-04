from time import perf_counter, sleep
from typing import Callable

def func_timer(func_object: Callable) -> Callable:
    """Выводит время выполнения переданной функции"""
    def wrapped(*args, **kwargs):
        t_start = perf_counter()
        res = func_object(*args, **kwargs)
        t_stop = perf_counter()
        res_time = t_stop - t_start
        print(f"\n\tФункция {func_object.__name__} выполнилась за {res_time:.5f} секунд")
        return res
    return wrapped

@func_timer
def report_func(time_left: int,
                interval: float) -> None:
    while time_left > 0:
        print(f'... {time_left}')
        sleep(interval)
        time_left -= 1
    print('\nBOOM!!!')
    
report_func(10, 0.5)


# stdout

# ... 10
# ... 9
# ... 8
# ... 7
# ... 6
# ... 5
# ... 4
# ... 3
# ... 2
# ... 1

# BOOM!!!

        # Функция report_func выполнилась за 5.07016 секунд