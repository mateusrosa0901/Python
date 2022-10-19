import random

lc = ['Pedra' , 'Papel' , 'Tesoura']
ec = random.choice(lc)

print('='*20)
print('1- Pedra')
print('2- Papel')
print('3- Tesoura')
print('='*20)

eu = int(input('Escolha sua jogada: '))

if eu == 1 and ec == 'Tesoura':
    print(f'Computador: {ec}')
    print(f'Jogador: Pedra')
    print(f'\033[32mParabéns\033 você ganhou!')

elif eu == 2 and ec == 'Pedra':
    print(f'Computador: {ec}')
    print('Jogador: Papel')
    print(f'\033[32mParabéns\033 você ganhou!')

elif eu == 3 and ec == 'Papel':
    print(f'Computador: {ec}')
    print('Jogador: ')