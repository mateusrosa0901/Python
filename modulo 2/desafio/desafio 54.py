from datetime import date, datetime
ma = 0
me = 0
for p in range(1,8):
    ano = int(input('Ano de nascimento: '))
    i = date.today().year - ano
    if i >= 21:
        ma += 1
    else:
        me += 1

print(f'{ma} pessoas são maiores de idade.')
print(f'{me} pessoas são menores de idade.')