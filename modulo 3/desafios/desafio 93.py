fichaJogador = dict()
gols = list()
totGols = int(0)

fichaJogador['nome'] = str(input('Digite o nome do jogador: '))

partidas = int(input(f'Quantas partidas o {fichaJogador["nome"]} jogou? '))

for p in range(partidas):
    gols.append(int(input(f'Quantos gols foram feitos na partida {p}? ')))

fichaJogador['gols'] = gols[:]

for g in gols:
    totGols += g

fichaJogador['total'] = totGols

print('-=-'*20)
for k, v in fichaJogador.items():
    print(f'{k}: {v}')

print('-=-'*20)
print(f'O jogador {fichaJogador["nome"]}, jogou {partidas} partidas:')
for g in range(len(gols)):
    print(f'   -> Na partida {g}, fez {gols[g]} gols.')
print(f'Um total de {totGols} gols.')
