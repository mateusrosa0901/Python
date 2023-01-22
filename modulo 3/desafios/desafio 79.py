valores = []
loop = str('')
num = int(0)

while loop != 'N':
    print('-'*40)
    num = int(input('Digite um número para adicionar à lista: '))
    if num not in valores:
        valores.append(num)
        print('° Valor adicionado °')

    else:
        print('# O valor digitado já está na lista #')

    loop = str(input('Deseja adicionar mais um valor? [S/N]: ')).strip().upper()[0]

    while loop != 'S' and loop != 'N':
        loop = str(input('Valor inválido, digite novamente [S/N]: ')).strip().upper()[0]

print('')
print('-'*20)
valores.sort()
print(f'valores digitados em ordem crescente: {valores}')
