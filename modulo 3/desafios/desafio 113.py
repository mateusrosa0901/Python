def leiaInt():
    while True:
        try:
            inteiro = int(input('Digite um número inteiro: '))

            return inteiro

        except ValueError:
            print('\033[1;91mTipo digitado inválido\033[m')

        except KeyboardInterrupt:
            print('\033[1;91mO usuário decidiu sair.\033[m')
            return 0


def leiaFloat():
    while True:
        try:
            real = float(input('Digite um número real: '))

            return real

        except ValueError:
            print('\033[1;91mTipo digitado inválido\033[m')

        except KeyboardInterrupt:
            print('\033[1;91mO usuário decidiu sair.\033[m')
            return 0


i = leiaInt()
r = leiaFloat()

print(f'O número inteiro digitado foi: {i}')
print(f'O número real digitado foi: {r}')
