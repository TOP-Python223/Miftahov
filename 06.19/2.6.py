count = 0
for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                for m in range(10):
                    for n in range(10):
                        if i + j + k == l + m + n:
                            count += 1
                            
print(f'Количество «счастливых» билетов: {count - 1}')