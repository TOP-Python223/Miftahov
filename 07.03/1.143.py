def anagramm(word):
    d = {}
    for elem in word:
        d[elem] = d.setdefault(elem, 0) + 1
    return d
    
word1, word2 = input('Введите первое слово: '), input('Введите второе слово: ')
check1, check2 = anagramm(word1), anagramm(word2) 


if check1 == check2:
    print('Слова являются анаграммами')
else:
    print('Слова не являются анаграммами')