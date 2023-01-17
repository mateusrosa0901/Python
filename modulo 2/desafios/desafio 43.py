peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

icm = peso / (altura**2)
print(f'{icm:.1f}')

if icm < 18.5:
    print('Abaixo do peso')
elif icm >= 18.5 and icm < 25:
    print('Peso ideal')
elif icm >= 25 and icm < 30:
    print('Sobrepeso')
elif icm >= 30 and icm < 40:
    print('Obesidade')
elif icm >= 40:
    print('Obesidade mórbida')