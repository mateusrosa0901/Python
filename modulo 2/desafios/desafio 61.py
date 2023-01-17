num = int(input('Digite o primeiro número da PA: '))
razao = int(input('Digite a razão: '))
termo = num
c = int(0)

while c <= 10:
    if c < 10:
        print(termo , end=' -> ')
    else:
        print(termo)
    termo += razao
    c += 1
