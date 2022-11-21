char_seq = ((6,2,'К'),(1,5,'У'),(3,3,'З'),(1,1,'Ь'),(7,4,'М'),(1,7,'А'))

for i in range(len(char_seq)):
    for n in range(char_seq[i][0]):
        for k in range(char_seq[i][1]):
            print(char_seq[i][2], end='')
        print()