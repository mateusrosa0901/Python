continuar = 'S'
n = 0
c = 0
s = 0

while continuar == 'S':
    print('='*50)
    n = int(input('Digite um número: '))
    c += 1
    s += n
    continuar = input('Você deseja continuar? [S/N]: ').upper()
    
    if continuar != 'S' and continuar != 'N':
        print('Valor inválido.')
        continuar = input('Você deseja continuar? [S/N]: ').upper()

print('='*50)
print(f'Média dos números digitados: {s/c}')
print(f'Soma dos números digitados: {s}')
print('='*50)
