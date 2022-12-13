continuar = 'S'
num = 0
cont = 0
soma = 0

while continuar == 'S':
    print('='*50)
    num = int(input('Digite um número: '))
    cont += 1
    soma += num
    continuar = input('Você deseja continuar? [S/N]: ').upper().strip()[0]
    
    if continuar != 'S' and continuar != 'N':
        print('Valor inválido.')
        continuar = input('Você deseja continuar? [S/N]: ').upper().strip()[0]

print('='*50)
print(f'Média dos números digitados: {soma/cont}')
print(f'Soma dos números digitados: {soma}')
print('='*50)
