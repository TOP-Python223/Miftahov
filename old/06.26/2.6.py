LISP_code = ''.join([i for i in input('Введите строку кода: ') if i in '()[]{}'])

while '()' in LISP_code or '[]' in LISP_code or '{}' in LISP_code:
    LISP_code = LISP_code.replace('()', "")
    LISP_code = LISP_code.replace('[]', "")
    LISP_code = LISP_code.replace('{}', "")

print(len(LISP_code) == 0)