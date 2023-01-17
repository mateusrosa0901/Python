idade = int(0)
sexo = str('')
loop = str('')
qtdMaiorIdade = int(0)
qtdHomens = int(0)
qtdMulherMenor = int(0)

while True:
    print('-=-'*20)
    idade = int(input('Digite sua idade: '))

    sexo = str(input('Digite seu sexo [F/M]: ')).strip().upper()[0]
    while sexo != 'F' and sexo != 'M':
        sexo = str(input('Valor inválido, digite novamente [F/M]: ')).strip().upper()[0]

    if idade >= 18:
        qtdMaiorIdade += 1

    if sexo == 'M':
        qtdHomens += 1

    if sexo == 'F' and idade < 20:
        qtdMulherMenor += 1

    loop = str(input('Você deseja cadastrar mais uma pessoa? [S/N]: ')).strip().upper()[0]
    while loop != 'S' and loop != 'N':
        loop = str(input('Valor inválido, digite novamente [S/N]: ')).strip().upper()[0]

    if loop == 'N':
        break

print('-=-'*20)


print(f'Quantidade de pessoas maiores de 18 anos: {qtdMaiorIdade}')
print(f'Quantidade de homens cadastrados: {qtdHomens}')
print(f'Quantidade de mulheres que tem menos de 20 anos: {qtdMulherMenor}')
