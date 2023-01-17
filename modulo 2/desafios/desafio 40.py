n1 = float(input('Digite a 1° nota: '))
n2 = float(input('Digite a 2° nota: '))

m = (n1 + n2) / 2
print(f'{m:.1f}')

if m <5:
    print('\033[31mREPROVADO\033')

elif m <= 6.9:
    print('\033[33mRECUPERAÇÃO\033')

elif m >= 7:
    print('\033[32mAPROVADO\033')
