nome = input('Digite seu nome: ')
separar = nome.split()

print(f'primeiro nome: {separar[0]}')
print(f'ultimo nome: {separar[len(separar)-1]}')