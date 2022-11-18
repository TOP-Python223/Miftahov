l, counter = [int(num) for num in input('Ведите числа через пробел: ').split()], 0
for i in range(len(l) - 1):
    if l[i] < l[i + 1]:
        counter += 1
print(counter)
    
    