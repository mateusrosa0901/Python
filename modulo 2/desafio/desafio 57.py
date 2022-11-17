s = input('Digite seu sexo[F/M]: ').upper()
while s != 'F' and s != 'M':
    print('='*20)
    print('Valor inválido, tente novamente.')
    s = input('Digite seu sexo[F/M]: ').upper()
    
print('FIM.')