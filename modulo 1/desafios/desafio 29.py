km = int(input('Velocidade (Km/h): '))
m = 0

if km > 80:
    m = (km-80)*7
    print(f'Total da multa: R${m:.2f}')
else:
    print('Dentro do limite de velocidade!')