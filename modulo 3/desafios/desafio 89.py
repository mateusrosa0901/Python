ficha = []
boletim = []
loop = str('')
id = int(0)

while True:
    print('='*25)
    nome = str(input('Digite o nome do aluno(a): '))
    nota1 = float(input('Digite a 1° nota: '))
    nota2 = float(input('Digite a 2° nota: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    boletim.append(ficha[:])
    ficha.clear()

    loop = str(input('Deseja adicionar mais uma ficha? [S/N]: ')).strip().upper()[0]

    while loop != 'S' and loop != 'N':
        loop = str(input('Deseja adicionar mais uma ficha? [S/N]: ')).strip().upper()[0]

    if loop == 'N':
        break

print(boletim)
print('id | nome | média')
for f in range(len(boletim)):
    print(f'{f} | {boletim[f][0][0]} | {boletim[f][0][2]:.1f}')

while True:
    id = int(input('Digite o ID do aluno para ver suas notas (999 para sair): '))

    if id == 999:
        break

    print(f'{id} | {boletim[id][0][0]} | {boletim[id][0][1]:.1f}')

print('FIM')
