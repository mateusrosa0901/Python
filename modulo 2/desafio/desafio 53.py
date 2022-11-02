frase = input('Digite uma frase: ').strip().upper()
p = frase.split()
j = ''.join(p)
i = ''

for l in range(len(j) -1, -1, -1):
    i += j[l]

if i == j:
    print(j,i)
    print('Essa frase é um palindromo.')
else:
    print(j,i)
    print('Essa frase não é um palindromo.')