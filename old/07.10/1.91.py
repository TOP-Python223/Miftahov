def ordinalDate(day: int, 
                month: int, 
                year: int,
                leap: bool = False):
    
    leap = year % 4 == 0 and year % 100 != 0 or year % 400  == 0
    days = 0
    
    d = {1: 31, 2: (28, 29)[leap], 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    
    for k,v in d.items():
        if k == month:
            days += day
            return f"{days}-й день"
        days += v

print(ordinalDate(int(input('Введите день: ')), int(input('Введите месяц: ')), int(input('Введите год: '))))


# Ввод:
# Введите день: 5
# Введите месяц: 10
# Введите год: 2020

# Вывод:
# 279