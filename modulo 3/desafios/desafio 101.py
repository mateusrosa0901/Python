import datetime


def votar(ano_nas):
    idade = datetime.date.today().year - ano_nas

    if 16 <= idade < 18:
        return 'Voto não obrigatório.'
    elif idade >= 18:
        return 'Voto obrigatório.'
    else:
        return 'Não pode votar.'

print('-'*10)
ano_nas = int(input('Digite seu ano de nascimento: '))
print(votar(ano_nas))
