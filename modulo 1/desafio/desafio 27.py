nome = input('Digite seu nome: ')
separar = nome.split()
ContSeparar = len(separar)

print(f'primeiro nome: {separar[0]}')
print(f'ultimo nome: {separar[ContSeparar-1]}')