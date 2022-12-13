num = int(input('Digite o termo: '))
razao = int(input('Digite a razão: '))
dist = int(0)
c = int(0)

while dist == num + (10-1) * razao:
    dist += 1
    num += razao
    print(num)
