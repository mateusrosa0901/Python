from datetime import date
ficha = dict()

ficha['nome'] = str(input('Digite seu nome: '))

anoNasc = int(input('Digite o ano de nascimento: '))
idade = date.today().year - anoNasc
ficha['idade'] = idade

ficha['ctps'] = int(input('Carteira de trabalho: '))

if ficha['ctps'] != 0:
    ficha['contrataçao'] = int(input('Ano da sua contratação: '))
    ficha['salario'] = float(input('Digite seu salário: R$'))
    diferença = date.today().year - ficha['contrataçao']
    idadeAposen = idade - diferença
    idadeAposen += 35
    ficha['idadeAposentado'] = idadeAposen

print('-=-'*20)
for k, v in ficha.items():
    print(f'{k}: {v}')
