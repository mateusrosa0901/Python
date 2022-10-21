from datetime import date
print('Qual o seu sexo:')
print('1- Masculino')
print('2- Feminino')
opção = int(input('-> '))
if opção == 1:
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

elif opção == 2:
    print('Mulheres não fazem alistamento militar no Brasil.')

else:
    print('Opção inválida')

