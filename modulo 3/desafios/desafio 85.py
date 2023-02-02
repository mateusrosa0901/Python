#numP = []
#numI = []
#num = []
#numAux = 0

#for c in range(0, 7):
#    numAux = int(input('Digite um número: '))
#    if numAux % 2 == 0:
#        numP.append(numAux)
#    else:
#        numI.append(numAux)

#numP.sort()
#numI.sort()
#num.append(numP[:])
#num.append(numI[:])

#print(num)

num = [[], []]
numAux = 0

for c in range(0, 7):
    numAux = int(input('Digite um número: '))
    if numAux % 2 == 0:
        num[0].append(numAux)
    else:
        num[1].append(numAux)

num[0].sort()
num[1].sort()
print(num)