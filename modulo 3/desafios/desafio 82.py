valores = []
valoresI = []
valoresP = []
loop = str('')

while loop != 'N':
    print('-=-' * 10)
    valores.append(int(input('Digite um valor: ')))

    loop = str(input('Deseja continuar?[S/N]: ')).strip().upper()[0]

    while loop != 'S' and loop != 'N':
        loop = str(input('Valor inválido, digite novamente [S/N]: ')).strip().upper()[0]

for n in valores:
    if n % 2 == 0:
        valoresP.append(n)
    else:
        valoresI.append(n)

print('')
print('-'*20)
print(f'Todos os valores: {valores}')
print(f'Valores pares: {valoresP}')
print(f'Valores ímpares: {valoresI}')