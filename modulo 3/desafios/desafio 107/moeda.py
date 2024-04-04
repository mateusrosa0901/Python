def aumentar(valor, pAumentar):
    valor = valor + (valor * pAumentar/100)

    return valor


def diminuir(valor, pDiminuir):
    valor = valor - (valor * pDiminuir/100)

    return valor


def dobro(valor):
    valor *= 2

    return valor


def metade(valor):
    valor /= 2

    return valor