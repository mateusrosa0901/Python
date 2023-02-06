linha1 = [[], [], []]
linha2 = [[], [], []]
linha3 = [[], [], []]
somaPar = int(0)
somaColuna = int(0)

for p in range(len(linha1)):
    linha1[p].append(int(input(f'Digite o conteúdo da posição (0,{p}): ')))

for p in range(len(linha2)):
    linha2[p].append(int(input(f'Digite o conteúdo da posição (1,{p}): ')))

for p in range(len(linha3)):
    linha3[p].append(int(input(f'Digite o conteúdo da posição (2,{p}): ')))

print(f'{linha1[0]} {linha1[1]} {linha1[2]}')
print(f'{linha2[0]} {linha2[1]} {linha2[2]}')
print(f'{linha3[0]} {linha3[1]} {linha3[2]}')

for n in linha1:
    if n[0] % 2 == 0:
        somaPar += n[0]
for n in linha2:
    if n[0] % 2 == 0:
        somaPar += n[0]
for n in linha3:
    if n[0] % 2 == 0:
        somaPar += n[0]

print(f'Soma dos números pares: {somaPar}')

somaColuna = linha1[2][0] + linha2[2][0] + linha3[2][0]

print(f'Soma da 3° coluna: {somaColuna}')
