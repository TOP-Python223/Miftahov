check = set(input('Введите строку: '))

binary = {'0', '1'}
others = {'2', '3', '4', '5', '6', '7', '8', '9'}

if check & others:
    print('НЕТ')
elif check >= binary:
    print('ДА')
else:
    print('НЕТ')




