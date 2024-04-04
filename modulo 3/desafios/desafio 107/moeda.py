def aumentar(valor, pAumentar, format=False):
    valor = valor + (valor * pAumentar / 100)

    if format:
        valor = moeda(valor)

    return valor


def diminuir(valor, pDiminuir, format=False):
    valor = valor - (valor * pDiminuir / 100)

    if format:
        valor = moeda(valor)

    return valor


def dobro(valor, format=False):
    valor *= 2

    if format:
        valor = moeda(valor)

    return valor


def metade(valor, format=False):
    valor /= 2

    if format:
        valor = moeda(valor)

    return valor


def moeda(valor):
    return f'R${valor:.2f}'
