num = int(0)
soma = int(0)
cont = int(0)

while num != 999:
    print('='*50)
    print('Para sair digite 999')
    num = int(input('Digite um número: '))
    if num != 999:
        soma += num
        cont += 1

print('='*50)
print(f'Você digitou {cont} números.')
print(f'{soma} é a soma desses números.')