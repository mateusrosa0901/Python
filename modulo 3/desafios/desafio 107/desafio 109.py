import moeda

valor = float(input('Digite o valor: R$'))

print(f'Metade de {moeda.moeda(valor)}: {moeda.metade(valor, True)}')
print(f'Dobro de {moeda.moeda(valor)}: R$ {moeda.dobro(valor, True)}')
print(f'Aumentando 20%: {moeda.aumentar(valor, 20, True)}')
print(f'Diminuindo 15%: {moeda.diminuir(valor, 15, True)}')