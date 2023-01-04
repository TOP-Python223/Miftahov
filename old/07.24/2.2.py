from typing import Callable
from random import randrange as rr
from datetime import datetime as dt

def logger(func_object: Callable) -> Callable:
    """Логирует вызов функции в файл-журнал"""
    def wrapped(*args, **kwargs):
        curr_time = dt.now()
        res = func_object(*args, **kwargs)
        
        with open("journal.txt", "a") as file:
            print(f"{curr_time}\t{func_object.__name__}\t", end='')
            file.write(f"{curr_time}\t{func_object.__name__}\t")
            if args:
                print(f"{args}\t", end='')
                file.write(f"{args}\t")
            if kwargs:
                print(f"{kwargs}\t", end='')
                file.write(f"{kwargs}\t")
            print(res)
            file.write(f"{res}\n")
        return res
    return wrapped

@logger
def checkhand(hand):
    """Возвращает старшую покерную комбинацию"""
    
    comb_label = 'старшая карта'
    
    unique = set(hand)
    u_len = len(unique)
    
    if u_len == 4:
        comb_label = 'пара'
    
    elif u_len == 3:
        if max([hand.count(card) for card in unique]) == 2:
            comb_label = 'две пары'
        else:
            comb_label = 'сет'
    
    elif u_len == 5:
        hand_sort = sorted(hand)
        if hand_sort == list(range(hand_sort[0], hand_sort[0]+5)):
            comb_label = 'стрит'
    
    elif u_len == 2:
        if max([hand.count(card) for card in unique]) == 3:
            comb_label = 'фулл-хаус'
        else:
            comb_label = 'каре'
    
    elif u_len == 1:
        comb_label = 'Шулер!'
    
    return comb_label

res = ''
while res.split('\t')[-1] != 'стрит':
    hand = tuple(rr(1, 14) for _ in range(5))
    res = checkhand(hand)



