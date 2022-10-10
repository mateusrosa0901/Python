ano = int(input('Digite um ano: '))

if ano % 100 == 0 and ano % 400 == 0:
    print(f'{ano} é um ano bissexto')

else:
    print(f'{ano} não é um ano bissexto')