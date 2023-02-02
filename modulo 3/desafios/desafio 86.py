linha1 = [[], [], []]
linha2 = [[], [], []]
linha3 = [[], [], []]

for p in range(len(linha1)):
    linha1[p].append(int(input(f'Digite o conteúdo da posição (0,{p}): ')))

for p in range(len(linha2)):
    linha2[p].append(int(input(f'Digite o conteúdo da posição (1,{p}): ')))

for p in range(len(linha3)):
    linha3[p].append(int(input(f'Digite o conteúdo da posição (2,{p}): ')))

print(f'{linha1[0]} {linha1[1]} {linha1[2]}')
print(f'{linha2[0]} {linha2[1]} {linha2[2]}')
print(f'{linha3[0]} {linha3[1]} {linha3[2]}')