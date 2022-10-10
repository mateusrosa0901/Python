n1 = int(input('1° número: '))
n2 = int(input('2° número: '))
n3 = int(input('3° número: '))

#n1 maior
if n1 > n2 and n1 > n3:
    print(f'{n1} é o maior número.')

#n2 maior
if n2 > n1 and n2 > n3:
    print(f'{n2} é o maior número.')

#n3 maior
if n3 > n1 and n3 > n2:
    print(f'{n3} é o maior número.')

#igual
if n1 == n2 and n1 == n3:
    print(f'Os três números são iguais.')