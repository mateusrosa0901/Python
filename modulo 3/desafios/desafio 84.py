dados = []
lista = []
loop = ''


while True:
    print('-'*20)
    dados.append(str(input('Digite o nome: ')))
    dados.append(float(input('Digite o peso [Kg]: ')))
    lista.append(dados[:])
    dados.clear()

    loop = str(input('Deseja cadastrar mais uma pessoa? [S/N]: ')).strip().upper()[0]
    while loop != 'S' and loop != 'N':
        loop = str(input('Deseja cadastrar mais uma pessoa? [S/N]: ')).strip().upper()[0]

    if loop == 'N':
        break


print(f'Quantidade de pessoas cadastradas: {len(lista)}')
