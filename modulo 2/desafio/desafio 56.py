nome = ''
idade = 0
sexo = ''
sidade = 0
velho = 0
nv = ''
nmv = 0
for p in range(1,5):
    print('='*30)
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    sexo = input('Seu sexo[F/M]: ')

    sidade += idade
    fs = sexo.strip().upper()
    if fs == 'M':
        if idade > velho:
            velho = idade
            nv = nome
    if fs == 'F':
        if idade < 20:
            nmv += 1

print('='*30)
print(f'Média das idades: {sidade/4}')
print(f'Nome do homem mais velho: {nv}')
print(f'{nmv} mulhere(s) tem menos de 20 anos.')
print('='*30)