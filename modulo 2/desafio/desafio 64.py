n = 0
s = 0
c = 0

while n != 999:
    print('='*50)
    print('Para sair digite 999')
    n = int(input('Digite um número: '))
    if n != 999:
        s += n
        c += 1
print(f'Você digitou {c} números.')
print(f'{s} é a soma desses números.')