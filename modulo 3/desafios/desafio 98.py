def contador1(i, f, p):
    for n in range(i, f+1, p):
        print(n, end=' -> ')
    print('FIM')

    print('-=-'*10)


def contador2(i, f, p):

    for n in range(i, f-1, p):
        print(n, end=' -> ')
    print('FIM')

    print('-=-'*10)


def contador3(i, f, p):

    if i > f:
        f -= 1
    else:
        f += 1

    p = mudaPasso(i, f, p)

    for n in range(i, f, p):
        print(n, end=' -> ')
    print('FIM')


def mudaPasso(i, f, p):
    if i > f and p >= -1:
        p *= -1
    if i < f and p <= -1:
        p *= -1
    if i > f and p == 0:
        p = -1
    elif i < f and p == 0:
        p = 1

    return p

contador1(1, 10, 1)
contador2(10, 0, -2)

ini = int(input('Digite o número de início: '))
fim = int(input('Digite o número de fim: '))
passo = int(input('Digite quantos números a contagem vai pular: '))

contador3(ini, fim, passo)
