n1 = input('Digite um número: ')
#mostrar qual o tipo de n1
print(f'tipo: {type(n1)}') 
#diz se tem apenas espaço
print(f'é espaço: {n1.isspace()}')
#diz se é número
print(f'é número: {n1.isnumeric()}')
#diz se é palavra
print(f'é palavra: {n1.isalpha()}')
#diz se tudo está maiusculo
print(f'tudo maiusculo: {n1.isupper()}')
#diz se tudo está minusculo
print(f'tudo minusculo: {n1.islower()}')