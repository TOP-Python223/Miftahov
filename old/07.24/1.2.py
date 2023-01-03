symbols = {'A', 'B', 'C'}


def my_perm(elements):
    """Генерирует в строковом виде перестановки для элементов переданного множества."""
    if not isinstance(elements, str):
        elements = ''.join(str(n) for n in elements)
    
    if len(elements) == 1:
        yield elements
    else:
        for elem in my_perm(elements[1:]):
            for i in range(len(elements)):
                yield elem[:i] + elements[0:1] + elem[i:] 
        

q = my_perm(symbols)
print(*sorted(q))


# stdout
# ABC ACB BAC BCA CAB CBA



