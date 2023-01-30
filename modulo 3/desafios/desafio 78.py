valores = []
maiorVal = 0
menorVal = int(0)
posMaiorVal = int(0)
posMenorVal = int(0)

for c in range(0,5):
    valores.append(int(input(f'Digite o {c+1}° valor: ')))
    if c == 0:
        maiorVal = valores[c]
        menorVal = valores[c]
        posMaiorVal = valores.index(maiorVal)
        posMenorVal = valores.index(menorVal)
    else:
        if valores[c] > maiorVal:
            maiorVal = valores[c]
            posMaiorVal = valores.index(maiorVal)

        if valores[c] < menorVal:
            menorVal = valores[c]
            posMenorVal = valores.index(menorVal)

print('')
print('-'*20)
print(f'\nlista: {valores}')

print(f'\n{maiorVal} é o maior valor e está na posição: ' , end=' ')

for pos , num in enumerate(valores):
    if num == maiorVal:
        print(f'{pos+1}°' , end=' ')

print(f'\n{menorVal} é o menor valor e está na posição: ' , end=' ')

for pos , num in enumerate(valores):
    if num == menorVal:
        print(f'{pos+1}°' , end=' ')