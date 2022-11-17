import random
c = 1

na = random.randrange(0,10)
nu = int(input('Digite um número de 0 a 10: '))
while nu != na:
    c += 1
    print('='*20)
    print('Você errou!')
    nu = int(input('Digite um número de 0 a 10: '))


print('Você acertou!')
print(f'Você tentou {c} vezes.')