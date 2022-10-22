from datetime import date
ano = int(input('Ano de nascimento: '))
idade = date.today().year - ano
print(f'Idade: {idade}')

if idade <= 9:
    print('MIRIM')

elif idade <= 14:
    print('INFANTIL')

elif idade <= 19:
    print('JUNIOR')

elif idade == 20:
    print('SÊNIOR')

elif idade > 20:
    print('MASTER')