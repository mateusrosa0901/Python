def func(b):
    global a
    print(f'a: {a}')
    a = 3
    print(f'b: {b}')
    print(f'a: {a}')
    print('fim da função')


a = 1

func(a)
print(f'a: {a}')