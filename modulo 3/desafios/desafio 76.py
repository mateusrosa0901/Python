lista = ('Lápis' , 1.50 , 'Caderno' , 9.8 , 'Mouse' , 12)

print('---------- LISTA DE PREÇOS ----------')

for c in range(len(lista)):
    if c % 2 == 0:
        print(f'{lista[c]:<3} ............R$ {lista[c+1]:>5.2f}')