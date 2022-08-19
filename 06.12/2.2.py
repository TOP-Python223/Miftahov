a = int(input('Введите ваш возраст: '))

if a <= 13:
    print('детство')
elif a > 13 and a <= 24:
    print('молодость')
elif a >= 25 and a <= 59:
    print('зрелость')
elif a >= 60:
    print('старость')