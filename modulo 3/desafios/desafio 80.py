valores = []

for c in range(0,5):
    num = int(input('Digite um número: '))

    if c == 0 or num > valores[-1]:
        valores.append(num)
    else:
        pos = 0
        while pos < len(valores):
            if num <= valores[pos]:
                valores.insert(pos , num)
                break
            pos += 1
print('')
print('-=-'*20)
print(valores)
