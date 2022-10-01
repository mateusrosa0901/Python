import math
a = int(input('Digite um ângulo: '))

#transforma ângulo em radiano para usar as funções do módulo
r = math.radians(a) 

print(f'seno: {math.sin(r):.2f}')
print(f'cosseno: {math.cos(r):.2f}')
print(f'tangente: {math.tan(r):.2f}')