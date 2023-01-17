s = input('Digite seu sexo[F/M]: ').upper().strip()[0]

while s != 'F' and s != 'M':
    print('='*20)
    print('Valor inválido, tente novamente.')
    s = input('Digite seu sexo[F/M]: ').upper().strip()[0]
    
if s == 'M':
    print('Sexo masculino registrado.')
else:
    print('Sexo feminino registrado.')
print('FIM.')