from itertools import count


frase = input('Digite uma frase: ')
mai = frase.upper()
contA = mai.count('A')

print(f'quantidadede A: {contA}')
print(f'posição do 1° A: {mai.find("A")}')
print(f'posição do ultimo A: {mai.rfind("A")}')