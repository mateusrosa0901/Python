from datetime import date


def votar(ano_nas):
    idade = date.today().year - ano_nas

    if 16 <= idade < 18:
        return [idade, 'VOTO OPCIONAL.']
    elif 18 <= idade < 65:
        return [idade, 'Voto obrigatório.']
    elif idade >= 65:
        return [idade, 'VOTO OPCIONAL.']
    else:
        return [idade, 'Não pode votar.']

print('-'*10)
ano_nas = int(input('Digite seu ano de nascimento: '))
resposta = votar(ano_nas)
print(f'{resposta[0]} Anos: {resposta[1]}')
