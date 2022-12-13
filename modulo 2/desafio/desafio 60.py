num = int(input('Digite um número e veja seu fatorial: '))
fatorial = num
numAux = num

while num > 1:
    num = num - 1
    fatorial = num * fatorial

print(f'{numAux}! = {fatorial}')
    