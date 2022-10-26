text, d = input("Введите текст: ").lower().split(), {}

for word in sorted(text):
    word = word.strip(",.!&:;_-\'\"")
    d[word] = d.get(word, 0) + 1
    
for i in d:
    if d[i] == min(d.values()):
        print(i)
        break
    

