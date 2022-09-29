import math
co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjascente: '))

s = co**2 + ca**2
h = math.sqrt(s)

print(f'A hipotenusa é: {h:.2f}')