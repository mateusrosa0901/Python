galera = []
dados = []

for c in range(0, 3):
    dados.append(str(input('Digite seu nome: ')))
    dados.append(int(input('Digite sua idade: ')))
    galera.append(dados[:])
    dados.clear()

print(galera)
