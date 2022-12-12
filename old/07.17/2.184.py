def list_flat(iterator: list) -> list:
    """Рекурсивная функция выравнивания списка"""
    if iterator:
        if isinstance(iterator[0], list):
            l1 = list_flat(iterator[0])
            l2 = list_flat(iterator[1:])
            return l1 + l2
        else:
            s1 = [iterator[0]]
            s2 = list_flat(iterator[1:])
            return s1 + s2
    else:
        return iterator
    

data = [[1, [2, 3], [4, [5, [6, 7]]], [[[8], 9], [10]]]]
data2 = [[[2, 4], [6, 7, 8, 9], [1, 3], [5, 6, 5, 4, 3, 1]]]
data3 = [['w', 'w', 'w'], ['o'], ['r'], ['l'], ['d'], ['g', 'g', 'g', 'g'], ['r'], ['e'], ['a'], ['t', 't'], ['e'], ['c', 'c'], ['h'], ['e'], ['m'], ['g', 'g'], ['p'], ['w', 'w']]
data4 = [[[[[1, 2, [3, 4, [5], 6], 7, [8, 9], 10], [11]], [12, [13, 14, [15, [16]]], 17, [[18, 19], 20]]], 21, [22, 23], 24], [25]]

print(list_flat(data))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list_flat(data2))
# [2, 4, 6, 7, 8, 9, 1, 3, 5, 6, 5, 4, 3, 1]

print(list_flat(data3))
# ['w', 'w', 'w', 'o', 'r', 'l', 'd', 'g', 'g', 'g', 'g', 'r', 'e', 'a', 't', 't', 'e', 'c', 'c', 'h', 'e', 'm', 'g', 'g', 'p', 'w', 'w']

print(list_flat(data4))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
