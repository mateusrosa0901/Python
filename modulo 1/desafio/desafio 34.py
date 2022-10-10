sala = float(input('Digite o valor do salário: R$'))
aum = 0
if sala >= 1250:
    aum = sala + (sala * 0.1)
    print(f'O novo salário passa a ser R${aum:.2f}')

else:
    aum = sala + (sala * 0.15)
    print(f'O novo salário passa a ser R${aum:.2f}')