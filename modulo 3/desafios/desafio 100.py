from random import sample

def sorteio(lst):
    numAl = sample(lst, 5)
    print(f'Números aleatórios: {numAl}')
    soma(numAl)


def soma(lst):
    sp = 0
    for n in lst:
        if n % 2 == 0:
            sp += n
    print(f'Soma dos números aleatórios pares: {sp}')


números = [1, 5, 6, 4, 7, 12, 45, 32, 15, 13]

sorteio(números)