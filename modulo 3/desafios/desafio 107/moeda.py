def aumentar(valor, pAumentar, format=False):
    valor = valor + (valor * pAumentar / 100)

    if format:
        return moeda(valor)

    return valor


def diminuir(valor, pDiminuir, format=False):
    valor = valor - (valor * pDiminuir / 100)

    if format:
        return moeda(valor)

    return valor


def dobro(valor, format=False):
    valor *= 2

    if format:
        return moeda(valor)

    return valor


def metade(valor, format=False):
    valor /= 2

    if format:
        return moeda(valor)

    return valor


def moeda(valor):
    return f'R${valor:.2f}'


def resumo(valor, pAumentar=0.0, pDiminuir=0.0):
    print('-'*35)
    print(f'{'Resumo':^35}')
    print('-'*35)

    dob = dobro(valor)
    m = metade(valor)
    a = aumentar(valor, pAumentar)
    d = diminuir(valor, pDiminuir)

    print(f'Valor analizado: {'R$':>4} {valor:<10,.2f}')
    print(f'Dobro do valor: {'R$':>5} {dob:<10,.2f}')
    print(f'Metade do valor: {'R$':>4} {m:<10,.2f}')
    print(f'{pAumentar:.1f}% de aumento: {'R$':>3} {a:<10,.2f}')
    print(f'{pDiminuir:.1f}% de redução: {'R$':>3} {d:<10,.2f}')
