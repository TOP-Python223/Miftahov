num_ticket = [int(num) for num in input('Введите номер билета: ')]
print('ДА' if sum(num_ticket[:3]) == sum(num_ticket[3:]) else 'НЕТ')