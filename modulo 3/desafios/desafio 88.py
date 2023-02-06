import random
from time import sleep

jogos = []
jogosAux = []
qtdJogos = int(0)
num = int(0)
cont = 1

qtdJogos = int(input('Quantos jogos você quer gerar? '))

for con in range(0, qtdJogos):
    for c in range(0, 6):
        num = random.randrange(61)
        while num in jogosAux:
            num = random.randrange(61)
        jogosAux.append(num)
    jogos.append(jogosAux[:])
    jogosAux.clear()

print('='*20)
print(f'- JOGOS -')
for jogo in jogos:
    print(f'jogo {cont}: {jogo[:]}')
    sleep(1)
    cont += 1
print('='*20)
