n = int(input('Digite um número: '))
verificação = n % 2

if verificação == 0:
    print(f'{n} é um número par!')
else:
    print(f'{n} é um número impar!')