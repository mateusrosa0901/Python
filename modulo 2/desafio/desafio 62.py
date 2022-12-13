num = int(input('Digite o primeiro número da PA: '))
razao = int(input('Digite a razão: '))
termo = num
limite = int(10)
loop = bool(True)
c = int(0)
cont = int(0)

while loop == True:

    while c <= limite:
        if c < 10:
            print(termo , end=' -> ')
        else:
            print(termo)
        termo += razao
        c += 1
        cont += 1

    limite = int(input('Quantos termos você quer mostrar? '))

    print('-=-' * 10)

    if limite > 0:
        loop = bool(True)
        c = 0    
    else:
        loop = bool(False)

print(f'Foi mostrado {cont} termos.')