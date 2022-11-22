o = 0
n1 = int(input('Digite o 1° número: '))
n2 = int(input('Digite o 2° número: '))
while o != 5:
    print('='*50)
    

    print('OPÇÕES')
    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior')
    print('[4] Novos números')
    print('[5] Sair')

    print('='*50)
    o = int(input('Escolha uma opção: '))
    print('='*50)

    if o > 5:
        while o > 5:
            o = int(input('Opção inválida, digite novamente: '))
    elif o == 1:
        print(f'{n1} + {n2} = {n1+n2}')
    elif o == 2:
        print(f'{n1} X {n2} = {n1*n2}')
    elif o == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}')
        else:
            print(f'{n2} é maior que {n1}')
    elif o == 4:
        n1 = int(input('Digite o 1° número: '))
        n2 = int(input('Digite o 2° número: '))
        
print('FIM')