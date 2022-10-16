from datetime import date
ano = int(input('Ano de nascimento: '))
idade = date.today().year - ano

if idade < 18:
    print('Ainda não chegou sua hora de se alistar.')
    print(f'Você deve se alistar em {(18-idade)+date.today().year}')

elif idade == 18:
    print('Já está no ano de você se alistar.')

elif idade > 18:
    print('Já passou o ano de você se alistar.')
    print(f'Você deveria se alistar em {(18-idade)+date.today().year}')