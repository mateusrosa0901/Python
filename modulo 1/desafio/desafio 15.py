km = float(input('Km rodado: '))
d = int(input('Dias alugados: '))

diaria = d * 60
kilomet = km * 0.15
tot = diaria + kilomet

print(f'Total: R${tot:.2f}')