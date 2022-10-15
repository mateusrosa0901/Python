n1 = int(input('Digite o 1° valor: '))
n2 = int(input('Digite o 2° valor: '))

if n1 > n2:
    maior = n1
    print(f'O número {maior} é maior')
elif n2 > n1:
    maior = n2
    print(f'O número {maior} é maior')
elif n2 == n1:
    print(f'Os valores são iguais.')