valor = int(input('Digite o valor que você deseja sacar: R$'))
total = valor
ced = int(50)
totced = int(0)

print('---------- RESUMO ----------')
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'{totced} notas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break

print('-'*28)