palavras = ('carro' , 'vaca' , 'lixo' , 'grama')

for p in palavras:
    print(f'\nA palavra {p.upper()} possui as vogais: ' , end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra , end='')