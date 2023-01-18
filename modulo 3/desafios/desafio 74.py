import random

num = (random.randrange(10) , random.randrange(10) , random.randrange(10) , random.randrange(10) , random.randrange(10))
numMaior = int(0)
numMenor = int(0)

print(f'Números aléatorios: {num}')

for c in range(len(num)):
    if c == 0:
        numMaior = num[c]
        numMenor = num[c]
    
    else:
        if num[c] > numMaior:
            numMaior = num[c]
        if num[c] < numMenor:
            numMenor = num[c]

print(f'Maior número: {numMaior}')
print(f'Menor número: {numMenor}')