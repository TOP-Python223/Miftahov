d = {'b': 1, 'a': 2, 'c': 3, 'x': 1, 'z': 3}
find_v, l = int(input('Введите значение: ')), []

for k, v in d.items():
    if v == find_v:
        l.append(k)
print(l)