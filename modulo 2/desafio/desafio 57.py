s = input('Digite seu sexo[F/M]: ').upper().strip()

while s != 'F' and s != 'M':
    print('='*20)
    print('Valor inválido, tente novamente.')
    s = input('Digite seu sexo[F/M]: ').upper().strip()
    
if s == 'M':
    print('Sexo masculino registrado.')
else:
    print('Sexo feminino registrado.')
print('FIM.')