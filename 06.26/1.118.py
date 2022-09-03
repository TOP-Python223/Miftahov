input_us, words = input('Введите текст: '), []
for i in input_us.split():
    q = i.lower().strip(' .,!?-—_"/\:;')
    words += [q]
if words == words[::-1]:
    print('Палиндром')
else:
    print('Не палиндром')

# Введите текст: Is it crazy how saying sentences backwards creates backwards sentences saying how crazy it is
# Палиндром

# Введите текст: Contractions include: don’t, isn’t, and wouldn’t.
# Не палиндром
