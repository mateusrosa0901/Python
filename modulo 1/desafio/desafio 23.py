
n = int(input('Digite um número de 0 a 9999: '))
U = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print(f'unidade: {U}')
print(f'dezena: {d}')
print(f'centena: {c}')
print(f'milhar: {m}')