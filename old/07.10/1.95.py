def capitalLetters(text: str):
    res = text
    for i in range(len(text)):
        if text[i] in '!?.':
            for j in range(i + 1, len(text)):
                if text[j].isalpha():
                    res = res[0: j] + res[j].upper() + res[j+1: len(res)]
                    break
        if text[i] == 'i':
            if text[i - 1] == ' ' and text[i + 1] == ' ' or text[i + 1] in "!?.’":
                res = res[0: i] + res[i].upper() + res[i+1: len(res)]
    return res
    
wr_text = input('Write text: ').strip().capitalize()

print(capitalLetters(wr_text))




# Ввод:
# what time do i have to be there? what’s the address? this time i’ll try to be on time!

# Вывод:
# What time do I have to be there? What’s the address? This time I’ll try to be on time!

    
