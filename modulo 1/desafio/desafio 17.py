import math
co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjascente: '))

h = math.hypot(co,ca)

print(f'A hipotenusa é: {h:.2f}')