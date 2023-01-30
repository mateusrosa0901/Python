expr = str(input('Digite a expressão: '))
paren = []

for p in expr:
    if p == '(':
        paren.append('(')
    elif p == ')':
        if len(paren) > 0:
            paren.pop()
        else:
            paren.append(')')
            break

if len(paren) == 0:
    print('Sua expressão está correta.')
else:
    print('Sua expressão está incorreta.')