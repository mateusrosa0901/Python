num = int(input('Digite um número: '))
divsi = 0

for c in range(1,num+1):
    if num % c == 0:
        divsi += 1   

if divsi == 2:
    print(f'{num} é um número primo.')
else:
    print(f'{num} não é um número primo.')