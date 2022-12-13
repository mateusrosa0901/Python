num = int(input('Digite um número e veja seu fatorial: '))
fatorial = num
numAux = num

while num > 1:
    num -= 1
    fatorial =  fatorial * num

print(f'{numAux}! = {fatorial}')
    