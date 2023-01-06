num = int(0)
soma = int(0)

while True:
    num = int(input('Digite um número: '))

    if num == 999:
        break

    else:
        soma += num

print(f'A soma dos números digitados é: {soma}')