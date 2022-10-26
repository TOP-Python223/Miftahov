d = {1: "A, E, I, L, N, O, R, S, T, U", 
     2: "D, G", 
     3: "B, C, M, P",
     4: "F, H, V, W, Y",
     5: "K",
     8: "J, X",
     10: "Q, Z"}
     
word = input("Введите слово: ").upper()

counter = 0

for char in word:
    for k, v in d.items():
        if char in v:
            counter += k
            break

print(f"Количество очков за слово {word}: {counter}")