n = int(input('Digite um número: '))
print('='*20)
print('1- Binário')
print('2- Octal')
print('3- Hexadecimal')
print('='*20)
base = int(input('Escolha a base para conversão: '))

if base == 1:
    print(bin(n))

elif base == 2:
    print(oct(n))

elif base == 3:
    print(hex(n))