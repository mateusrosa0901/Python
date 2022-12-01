import random
c = 1
na = random.randrange(0,10)
nu = int(input('Digite um número de 0 a 10: '))

if nu > na:
    print('Menos... Tente novamente.')
elif nu < na:
    print('Mais... Tente novamente.')

while nu != na:
    c += 1
    print('='*20)
    print('Você errou!')
    nu = int(input('Digite um número de 0 a 10: '))
    if nu > na:
        print('Menos... Tente novamente.')
    elif nu < na:
        print('Mais... Tente novamente.')


print('Você acertou!')
print(f'Você tentou {c} vezes.')