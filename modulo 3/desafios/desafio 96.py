def area(l, c):
    a = l * c
    print(f'Valor da área é {a}m²')


larg = float(input('Digite a largura [m]: '))
compr = float(input('Digite o comprimento [m]: '))
print('-=-'*10)
area(larg, compr)
