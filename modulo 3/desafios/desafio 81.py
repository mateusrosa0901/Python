valores = []
loop = str('')

while loop != 'N':
    print('-=-'*10)
    valores.append(int(input('Digite um valor: ')))

    loop = str(input('Deseja continuar?[S/N]: ')).strip().upper()[0]

    while loop != 'S' and loop != 'N':
        loop = str(input('Valor inválido, digite novamente [S/N]: ')).strip().upper()[0]

print('')
print('-'*20)
print(f'Quantidade de valores digitados: {len(valores)}')

valores.sort(reverse=True)
print(f'Valores em ordem decrescente: {valores}')

if 5 in valores:
    print(f'O valor 5 foi digitado.')
else:
    print(f'O valor 5 não foi digitado.')
