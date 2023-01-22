valores = []

for c in range(0,5):
    num = int(input(f'Digite o {c+1}° valor: '))

    if c == 0:
        valores.append(num)

    else:
        for n in range(0 , len(valores)):
            if num > valores[n]:
                valores.insert(n+1 , num)

print(valores)