km = int(input('Distância da viagem (Km/h): '))

if km > 200:
    v = 0.45 * km
    print(f'Valor: {v}')
else:
    v = 0.5 * km
    print(f'Valor: {v}')