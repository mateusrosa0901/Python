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
print(f'lista: {valores}')
print(f'{maiorVal} é o maior valor e está na {posMaiorVal+1}° posição.')
print(f'{menorVal} é o menor valor e está na {posMenorVal+1}° posição.')