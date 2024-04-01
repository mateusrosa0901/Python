def ficha(nomeJogador="<desconhecido>", nGols=0):
    if nGols == '':
        nGols = 0

    return f'O jogador {nomeJogador}, fez {nGols} gol(s) no campeonato.'

print('-'*20)
nomeJogador = str(input('Nome do jogador: '))
nGols = input('Número de gols: ')


print(ficha(nomeJogador, nGols))