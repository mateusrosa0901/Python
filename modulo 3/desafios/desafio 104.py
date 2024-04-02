def leiaInt():
    '''
    Lê um número inteiro e caso ocorra um ValueError repete a leitura.
    :return: O número inteiro digitado
    '''
    print('-'*20)
    while True:
        try:
            num = int(input('Digite um número inteiro: '))

            return num

        except ValueError:
            print(f'\033[1;31mTipo inválido digite novamente\033[m')

help(leiaInt)
print(f'Numero digitado: {leiaInt()}')
