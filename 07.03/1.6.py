text = "1.py 1.py aux.h main.cpp functions.h main.cpp 2.py main.cpp".split()
d, res = {}, []

for f in text:
    d[f] = d.get(f, 0) + 1
    
for word in text[::-1]:
    if d[word] == 1:
        res.append(word)
        continue
    res.append(word.replace('.', f'_{d[word]}.'))
    d[word] -= 1
    
print(*res[::-1])