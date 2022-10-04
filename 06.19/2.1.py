email = input('Введите email: ')

print('Верно' if '@' in email and '.' in email[email.index('@') + 1:] else 'Неверно')