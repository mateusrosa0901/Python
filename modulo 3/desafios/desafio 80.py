valores = []

for c in range(0,5):
    num = int(input(f'Digite o {c+1}° valor: '))
    if c == 0:
        valores.append(num)
    else:
        for n in range(len(valores)):
            if num > valores[n] and num < valores[n+1]:
                valores.insert(valores.index(n+1) , num)
            #if num < n:
                #valores.insert(valores.index(n) , num)

print(valores)