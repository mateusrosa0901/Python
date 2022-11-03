ma = 0
me = ma

for p in range(0,6):
    peso = float(input('Digite o seu peso: '))
    #igualar as variaveis e depois trabalhar com elas
    if p == 0:
        ma = peso
        me = peso
    if peso >= ma:
        ma = peso
    elif peso <= me:
        me = peso

print(f'Maior peso: {ma:.1f}Kg')
print(f'Menor peso: {me:.1f}Kg')