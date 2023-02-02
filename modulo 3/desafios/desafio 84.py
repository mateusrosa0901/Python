dados = []
lista = []
loop = ''
maiorPeso = 0
menorPeso = 0
cont = 0

while True:
    print('-'*20)
    nome = str(input('Digite o nome: '))
    peso = float(input('Digite o peso [Kg]: '))
    dados.append(nome)
    dados.append(peso)
    lista.append(dados[:])
    dados.clear()

    if cont == 0:
        maiorPeso = peso
        menorPeso = peso
    else:
        if peso > maiorPeso:
            maiorPeso = peso
        if peso < menorPeso:
            menorPeso = peso

    loop = str(input('Deseja cadastrar mais uma pessoa? [S/N]: ')).strip().upper()[0]
    while loop != 'S' and loop != 'N':
        loop = str(input('Deseja cadastrar mais uma pessoa? [S/N]: ')).strip().upper()[0]

    if loop == 'N':
        break

    cont += 1

print('')
print('-=-'*10)
print(f'Quantidade de pessoas cadastradas: {len(lista)}')

print(f'Nome das pessoas mais pesadas: {maiorPeso:.2f}Kg', end=' ')
for p in lista:
    if p[1] == maiorPeso:
        print(p[0], end='; ')

print(f'\nNome das pessoas mais leves: {menorPeso:.2f}Kg', end=' ')
for p in lista:
    if p[1] == menorPeso:
        print(p[0], end='; ')
