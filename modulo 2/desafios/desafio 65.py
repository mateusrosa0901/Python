continuar = 'S'
num = 0
cont = 0
soma = 0
maior = 0
menor = 0

while continuar == 'S':
    print('='*50)
    num = int(input('Digite um número: '))
    cont += 1
    soma += num
    if cont == 1:
        maior = num
        menor = num
    
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    continuar = input('Você deseja continuar? [S/N]: ').upper().strip()[0]
    
    while continuar != 'S' and continuar != 'N':
        print('Valor inválido.')
        continuar = input('Você deseja continuar? [S/N]: ').upper().strip()[0]

print('='*50)
print(f'Média dos números digitados: {soma/cont}')
print(f'Soma dos números digitados: {soma}')
print(f'Maior número digitado: {maior}')
print(f'Menor número digitado: {menor}')
print('='*50)
