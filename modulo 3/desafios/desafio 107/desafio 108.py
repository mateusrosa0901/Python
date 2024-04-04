import moeda

valor = float(input('Digite o valor: R$'))

print(f'Metade de {moeda.moeda(valor)}: {moeda.moeda(moeda.metade(valor))}')
print(f'Dobro de {moeda.moeda(valor)}: {moeda.moeda(moeda.dobro(valor))}')
print(f'Aumentando 20%: {moeda.moeda(moeda.aumentar(valor, 20))}')
print(f'Diminuindo 15%: {moeda.moeda(moeda.diminuir(valor, 15))}')
