termos = int(input('Quantos termos você deseja mostrar: '))
cont = int(0)
sequ = int(0)
ant1 = int(0)
ant2 = int(1)

print(ant1)
print(ant2)

while cont != termos:
    sequ = ant1 + ant2
    print(sequ)

    ant1 = ant2
    ant2 = sequ

    cont += 1

print('FiM')
