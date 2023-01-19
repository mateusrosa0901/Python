n1 = int(input('Digite o 1° valor: '))
n2 = int(input('Digite o 2° valor: '))
n3 = int(input('Digite o 3° valor: '))
n4 = int(input('Digite o 4° valor: '))

num = (n1 , n2 , n3 , n4)

print('-'*20)
print(f'O número 9 apareceu {num.count(9)} vezes.')

if 3 in num:
    print(f'O número 3 apareceu primeiro na posição {num.index(3)}.')
else:
    print(f'O número 3 não foi digitado.')

print('Números pares digitados: ' , end='')

for c in range(len(num)):
    if num[c] % 2 == 0:
        print(num[c] , end=' ')