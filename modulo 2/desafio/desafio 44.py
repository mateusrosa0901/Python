vproduto = float(input('Digite o valor do produto: R$'))

print('='*20)
print('1- À vista dinheiro/cheque')
print('2- Cartão')
print('3- 2x no cartão')
print('4- 3x ou mais')
print('='*20)

pagamento = int(input('Escolha a forma de pagamento: '))

if pagamento == 1:
    print(f'Total: R${vproduto-(vproduto*0.1):.2f}')

elif pagamento == 2:
    print(f'Total: R${vproduto-(vproduto*0.05)}')

elif pagamento == 3:
    print(f'Total: R${vproduto}')

elif pagamento == 4:
    print(f'Total: R${vproduto+(vproduto*0.2)}')