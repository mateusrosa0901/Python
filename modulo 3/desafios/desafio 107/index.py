import moeda

valor = float(input('Digite o valor: R$ '))

print(f'Metade de R$ {valor}: R$ {moeda.metade(valor)}')
print(f'Dobro de R$ {valor}: R$ {moeda.dobro(valor)}')
print(f'Aumentando 20%: R$ {moeda.aumentar(valor, 20)}')
print(f'Diminuindo 15%: R$ {moeda.diminuir(valor, 15)}')
