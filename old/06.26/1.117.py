input_us, words = input('Введите текст: '), []
for i in input_us.split():
    q = i.strip('.,!?-—_"/\:;')
    words += [q]
print(words)
    
    
# Введите текст: Contractions include: don’t, isn’t, and wouldn’t.
# ['Contractions', 'include', 'don’t', 'isn’t', 'and', 'wouldn’t']