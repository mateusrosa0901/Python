import random

na = random.randrange(0,6)
nu = int(input('Digite um número entre 0 e 5: '))

if nu == na:
    print('Você acertou! 😀')
else:
    print('Você errou! 😥')