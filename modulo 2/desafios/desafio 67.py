valTabuada = int(0)
cont = int(0)

while True:
    print('-=-'*20)
    valTabuada = int(input('Digite o valor da tabuada: '))

    if valTabuada < 0:
        break

    else:
        cont = int(0)
        while cont != 10:
            cont += 1
            print(f'{valTabuada} X {cont} = {valTabuada * cont}')

print('-=-'*20)
print('FIM')