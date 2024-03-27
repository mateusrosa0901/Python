import datetime


def votar(ano_nas):
    idade = datetime.date.today().year - ano_nas

    if 16 <= idade < 18:
        return [idade, 'Voto não obrigatório.']
    elif idade >= 18:
        return [idade, 'Voto obrigatório.']
    else:
        return [idade, 'Não pode votar.']

print('-'*10)
ano_nas = int(input('Digite seu ano de nascimento: '))
resposta = votar(ano_nas)
print(f'{resposta[0]} Anos: {resposta[1]}')
