from datetime import date
ficha = dict()

ficha['nome'] = str(input('Digite seu nome: '))

anoNasc = int(input('Digite o ano de nascimento: '))
idade = date.today().year - anoNasc
ficha['idade'] = idade

ficha['ctps'] = str(input('Carteira de trabalho: '))

if ficha['ctps'] != 0:
    ficha['anoContrato'] = int(input('Ano da sua contratação: '))
    ficha['salario'] = float(input('Digite seu salário: R$'))
    diferença = date.today().year - ficha['anoContrato']
    idadeAux = idade - diferença
    for c in range(0, 35):
        idadeAux += 1
    ficha['idadeAposentado'] = idadeAux

for k, v in ficha.items():
    print(f'{k}: {v}')

