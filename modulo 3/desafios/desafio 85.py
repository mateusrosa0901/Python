numP = []
numI = []
num = []
numAux = 0

for c in range(0, 7):
    numAux = int(input('Digite um número: '))
    if numAux % 2 == 0:
        numP.append(numAux)
    else:
        numI.append(numAux)

num.append(numP[:])
num.append(numI[:])

print(num)