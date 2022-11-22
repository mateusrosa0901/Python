n = int(input('Digite um número para saber seu fatorial: ') )

f = 1
c = 1

while c <= n:
    f *= c
    c += 1

print(f)