ma = 0
me = 99999999

for p in range(0,6):
    peso = float(input('Digite o seu peso: '))

    if peso >= ma:
        ma = peso
    elif peso <= me:
        me = peso

print(f'Maior peso: {ma:.1f}Kg')
print(f'Menor peso: {me:.1f}Kg')