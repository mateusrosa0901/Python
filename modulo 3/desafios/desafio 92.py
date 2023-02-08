import datetime
ficha = dict()

ficha['nome'] = str(input('Digite seu nome: '))
anoNasc = int(input('Digite o ano de nascimento: '))
idade = datetime.datetime.year - anoNasc

print(idade)