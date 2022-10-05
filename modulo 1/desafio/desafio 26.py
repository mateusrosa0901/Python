from itertools import count


frase = input('Digite uma frase: ')
formatar = frase.upper().strip()
contA = formatar.count('A')

print(f'quantidadede A: {contA}')
print(f'posição do 1° A: {formatar.find("A")+1}')
print(f'posição do ultimo A: {formatar.rfind("A")+1}')