def contador(i, f, p):

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

contador(1, 10, 1)
contador(10, 0, -2)

ini = int(input('Digite o número de início: '))
fim = int(input('Digite o número de fim: '))
passo = int(input('Digite quantos números a contagem vai pular: '))

contador(ini, fim, passo)
