def leiaInt():
    print('-'*20)
    while True:
        try:
            num = int(input('Digite um número inteiro: '))

            return num

        except ValueError:
            print(f'\033[1;31mTipo inválido digite novamente\033[m')


print(f'Numero digitado: {leiaInt()}')
