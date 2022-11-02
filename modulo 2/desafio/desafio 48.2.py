ca = 0
for c in range(1,501):
    print(c)
    if c % 2 == 1:
        if c % 3 == 0:
            ca += c

print(f'Resultado: {ca}')