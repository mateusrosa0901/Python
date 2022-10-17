from xmlrpc.client import boolean


r1 = float(input('1° reta: '))
r2 = float(input('2° reta: '))
r3 = float(input('3° reta: '))

if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
    true = print('Essas retas podem formar um triângulo.')

else:
    print('Essas retas não podem formar um triângulo.')

if 'Essas retas podem formar um triângulo.' in true:
    if r1 == r2 and r2 == r3:
        print('Equilátero')
    elif r1 == r2 and r1 != r3 or r3 == r1 and r3 != r2 or r3 == r2 and r3 != r1:
        print('Isósceles')
    elif r1 != r2 and r1 != r3:
        print('Escaleno')
