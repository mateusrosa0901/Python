n = 1
i = 0
p = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            p += 1
        else:
            i += 1

print(f'Números ímpares: {i}')
print(f'Números pares: {p}')