estado = dict()
brasil = list()

for c in range(0,3):
    estado['UF'] = str(input('Nome do estado: '))
    estado['Sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())

print(brasil)