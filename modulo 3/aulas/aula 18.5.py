galera = []
dados = []

for c in range(0, 3):
    dados.append(str(input('Digite seu nome: ')))
    dados.append(int(input('Digite sua idade: ')))
    galera.append(dados[:])
    dados.clear()

print(galera)

for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade.')
    else:
        print(f'{p[0]} é menor de idade.')
