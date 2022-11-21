text, vowels, chars = input('Введите текст: ').lower(), 'aeiou', '.,!?'

if text[-1] in chars:
    char = text[-1]
    text = text[:-1]
else:
    char = ''

if text[0] in vowels:
    print(text.capitalize() + 'way' + char)
else:
    while text[0] not in vowels:
        text = text[1:] + text[0]
    print(text.capitalize() + 'ay' + char)