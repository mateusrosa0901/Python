peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

icm = peso / (altura*altura)
print(icm:.2f)

if icm < 18.5:
    print('Abaixo do peso')
elif icm >= 18.5 or icm < 25:
    print('Peso ideal')
elif icm >= 25 or icm < 30:
    print('Sobrepeso')