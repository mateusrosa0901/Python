def leiaNome():
    while True:
        try:
            nome = str(input('Nome: ')).strip().capitalize()
            return nome

        except ValueError:
            print('\033[1;91mTipo digitado inválido.\033[m')


def leiaIdade():
    while True:
        try:
            idade = int(input('Idade: '))
            return idade

        except ValueError:
            print('\033[1;91mTipo digitado inválido.\033[m')


def leiaOpcao():
    while True:
        try:
            opcao = int(input('\033[1;92mSua opção: \033[m'))
            return opcao

        except ValueError:
            print('\033[1;91mTipo digitado inválido.\033[m')