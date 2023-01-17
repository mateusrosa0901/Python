import random

numJogador = int(0)
numComputador = int(0)
escolhaJogador = ''
soma = int(0)
contVitoria = int(0)


while True:
    print('-=-'*20)
    numJogador = int(input('Digite sua jogada: '))
    escolhaJogador = str(input('Escolha sua jogada [I/P]: ')).upper().strip()[0]
    print('-=-'*20)

    while escolhaJogador != 'I' and escolhaJogador != 'P':
        print('-=-'*20)
        escolhaJogador = str(input('Valor inválido, digite novamente[I/P]: ')).upper().strip()[0]

    numComputador = int(random.randrange(11)) 

    soma = numJogador + numComputador

    if soma % 2 == 0 and escolhaJogador == 'P':
        print('você venceu')
        contVitoria += 1

    elif soma % 2 != 0 and escolhaJogador == 'I':
        print('você venceu')
        contVitoria += 1

    else:
        print('você perdeu')
        break

print(f'Você teve {contVitoria} vitórias consecutivas.')