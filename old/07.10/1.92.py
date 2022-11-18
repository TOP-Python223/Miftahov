def calendarDate(year: int, 
                 ord_date: int, 
                 leap: bool = False):
    
    guarant_date = ord_date + 180
    # гарантия на товар 180 дней
    
    while guarant_date > 0: 
        leap = year % 4 == 0 and year % 100 != 0 or year % 400  == 0
        d = {1: 31, 2: (28, 29)[leap], 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    
        for k,v in d.items():
            if guarant_date - v < 0:
                return guarant_date, k, year
            guarant_date -= v
        year += 1

day, month, year  = calendarDate(int(input('Введите год: ')), int(input('Введите порядковый номер дня: ')))

print(f"\nОкончание гарантии на товар: {str(day).rjust(2, '0')}.{str(month).rjust(2, '0')}.{str(year)}")




# Ввод:
# Введите год: 2020
# Введите порядковый номер дня: 265

# Вывод:
# Окончание гарантии на товар: 20.03.2021