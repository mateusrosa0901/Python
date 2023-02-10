ficha = {}
jogadores = []
gols = []
totGols = int(0)
cod = int(0)

while True:
    ficha['nome'] = str(input('Digite o nome do jogador: '))

    partidas = int(input(f'Quantas partidas o {ficha["nome"]} jogou? '))

    for p in range(partidas):
        gols.append(int(input(f'Quantos gols foram feitos na partida {p}? ')))

    ficha['gols'] = gols[:]

    ficha['total'] = sum(gols)
    totGols = int(0)

    jogadores.append(ficha.copy())
    ficha.clear()

    loop = str(input('Adicionar mais uma pessoa: [S/N]: ')).strip().upper()[0]

    while loop != 'S' and loop != 'N':
        loop = str(input('Adicionar mais uma pessoa: [S/N]: ')).strip().upper()[0]
    print('-'*25)

    if loop == 'N':
        break
print('-=-'*20)
print('id | nome | gols por partida | total')
for j in range(len(jogadores)):
    print(f'{j} | {jogadores[j]["nome"]} | {jogadores[j]["gols"]} | {jogadores[j]["total"]}')

while cod != 999:
    cod = int(input('Digite o id para ver mais detalhes: '))

    while cod > len(jogadores) - 1 and cod != 999:
        cod = int(input('Digite o id para ver mais detalhes: '))

    if cod == 999:
        break

    print(f'O jogador {jogadores[cod]["nome"]}, jogou {len(jogadores[cod]["gols"])} partidas:')
    for g in range(len(jogadores[cod]["gols"])):
        print(f'   -> Na partida {g}, fez {jogadores[cod]["gols"][g]} gols.')
    print(f'Um total de {jogadores[cod]["total"]} gols.')

    print('='*30)
