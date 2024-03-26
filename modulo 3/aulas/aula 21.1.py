def contador(i, f, p):
    '''
    Faz uma contagem e retorna em forma de lista.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: lista com a contagem
    '''

    lst = list()

    if i > f:
        f -= 1
    else:
        f += 1

    p = mudaPasso(i, f, p)

    for n in range(i, f, p):
        lst.append(n)

    return lst


def mudaPasso(i, f, p):
    if i > f and p >= -1:
        p *= -1
    elif i < f and p <= -1:
        p *= -1
    elif i > f and p == 0:
        p = -1
    elif i < f and p == 0:
        p = 1

    return p

help(contador)

lstContagem = contador(1, 10, 5)

for n in lstContagem:
    print(n, '->', end=' ')
print('FIM')