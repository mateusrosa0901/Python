from random import randint

cont = 1
jogadores = dict()

jogadores['jogador1'] = randint(1, 6)
jogadores['jogador2'] = randint(1, 6)
jogadores['jogador3'] = randint(1, 6)
jogadores['jogador4'] = randint(1, 6)

for j in sorted(jogadores, key= jogadores.get, reverse= True):
    print(f'O {j} ficou em {cont}° lugar: {jogadores[j]}')
    cont += 1
