pessoa = []
pessoa.append('Mateus')
pessoa.append(18)
galera =[]
galera.append(pessoa[:])
pessoa[0] = 'victor'
pessoa[1] = 19
galera.append(pessoa[:])
print(pessoa)
print(galera)