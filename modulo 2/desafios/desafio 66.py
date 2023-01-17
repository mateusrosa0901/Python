num = int(0)
soma = int(0)
cont = int(0)

while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break

    else:
        soma += num
        cont += 1

print(f'A soma dos {cont} números digitados é {soma}')