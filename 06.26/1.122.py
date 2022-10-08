text, vowels = input('Введите текст: '), 'aeiou'

if text[0] in vowels:
    print(text + 'way')
else:
    while text[0] not in vowels:
        text = text[1:] + text[0]
    print(text + 'ay')

