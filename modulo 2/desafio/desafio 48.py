ca = 0
for c in range(3,501,3):
    print(c)
    if c % 2 == 1:
        ca = ca + c
    
print(f'resultado: {ca}')