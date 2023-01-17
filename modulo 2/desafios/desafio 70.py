nomeProduto = str('')
valorProduto = float(0)
loop = str('')
total = float(0)
produtoCaro = int(0)
nomeProdutoBarato = str('')
valorProdutoBarato = float(0)
cont = int(0)

while True:
    print('-=-'*20)

    nomeProduto = str(input('Nome do produto: '))

    valorProduto = float(input('Valor do produto: R$'))


    total += valorProduto

    if cont == 0:
        valorProdutoBarato = valorProduto
        nomeProdutoBarato = nomeProduto

    if valorProduto >= 1000:
        produtoCaro += 1

    if valorProduto < valorProdutoBarato:
        valorProdutoBarato = valorProduto
        nomeProdutoBarato = nomeProduto

    cont += 1

    loop = str(input(('Deseja continuar? [S/N]: '))).strip().upper()[0]
    while loop != 'S' and loop != 'N':
        loop = str(input('Valor inválido, digite novamente [S/N]: ')).strip().upper()[0]

    if loop == 'N':
        break

print('-=-'*20)

print(f'Total da compra: R${total}')
print(f'Quantidade de produtos que custam mais que R$1000: {produtoCaro}')
print(f'O {nomeProdutoBarato} é o produto mais barato e custa R${valorProdutoBarato}')