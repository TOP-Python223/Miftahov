telegram1 = input('Напишите телеграмму: ')
cost = 0
for i in telegram1:
    if i != ' ':
        cost += 80
        
print(f'{cost // 100} руб. {cost % 100} коп.')