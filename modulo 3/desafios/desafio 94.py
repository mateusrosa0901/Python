ficha = {}
pessoas = []
mulheres = []
idadeMM = []
loop = str('')
somaIdade = int(0)

while True:
    nome = str(input('Digite o nome: ')).strip()

    sexo = str(input('Digite o sexo [F/M]: ')).strip().upper()[0]
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Digite o sexo [F/M]: ')).strip().upper()[0]

    idade = int(input('Digite a idade: '))

    ficha['nome'] = nome
    ficha['sexo'] = sexo
    ficha['idade'] = idade

    pessoas.append(ficha.copy())
    ficha.clear()

    loop = str(input('Adicionar mais uma pessoa: [S/N]: ')).strip().upper()[0]
    while loop != 'S' and loop != 'N':
        loop = str(input('Adicionar mais uma pessoa: [S/N]: ')).strip().upper()[0]
    print('-'*25)
    if loop == 'N':
        break

for p in range(len(pessoas)):
    somaIdade += pessoas[p]['idade']

mediaIdade = somaIdade / len(pessoas)

for p in range(len(pessoas)):
    if pessoas[p]['sexo'] == 'F':
        mulheres.append(pessoas[p]['nome'])

print('-=-'*20)
print(f'Quantidade de pessoas cadastradas: {len(pessoas)}')
print(f'A média de idade das pessoas cadastra: {mediaIdade:.1f}')
print(f'Nome das mulheres cadastradas: {mulheres}')
print(f'Pessoas com a idade acima da média: ', end='')
for p in range(len(pessoas)):
    if pessoas[p]['idade'] > mediaIdade:
        print(f'{pessoas[p]["nome"]}: {pessoas[p]["idade"]} anos', end=', ')
