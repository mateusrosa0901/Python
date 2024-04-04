from time import sleep
def inicio():
    while True:
        sleep(1)
        print('\033[1;97;45m='*200)
        print('PROGRAMA PyHelp')
        print('=' * 200)

        sleep(1)
        func = str(input('\033[mFunção >> '))
        if func == 'sair':
            sair()
            break

        pyHelp(func)


def pyHelp(func):
    sleep(0.5)
    print('\033[1;97;46m-' * 200)
    print(f'Acessando manual do \033[1;93;46m{func}\033[1;97;46m')
    print('-' * 200, '\033[1;40;47m')

    sleep(0.5)
    return help(func)


def sair():
    sleep(0.5)
    print('\033[1;97;41m=' * 200)
    print('Até mais tarde :)')
    print('=' * 200)


inicio()
