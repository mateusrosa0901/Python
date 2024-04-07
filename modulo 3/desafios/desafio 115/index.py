from utils import dados, cadastro

def menuPrincipal():
    escolhas = [
        'Ver pessoas cadastradas',
        'Cadastrar nova pessoa',
        'Sair do sistema'
    ]
    opcao = int()

    print('-'*50)
    print('MENU PRINCIPAL'.center(50))
    print('-'*50)

    for e in range(len(escolhas)):
        print(f'\033[1;93m{e+1}\033[1;97m - \033[1;94m{escolhas[e]}\033[m')

    print('-' * 50)

    while opcao not in [1, 2, 3]:
        opcao = dados.leiaOpcao()

    match opcao:
        case 1: listarCadastros()
        case 2: novoCadastro()
        case 3: sair()

def novoCadastro():
    print('\033[1;95m-' * 50)
    print('NOVO CADASTRO'.center(50))
    print(f'{'-' * 50}\033[m')

    nome = dados.leiaNome()
    idade = dados.leiaIdade()

    c = cadastro.cadastrar(nome, idade)

    if c[0] == 'sucesso':
        menuPrincipal()
    else:
        erro(c[1])


def listarCadastros():
    data = cadastro.listar()
    if data[0] == 'sucesso':

        print('\033[1;96m-' * 50)
        print('LISTA DE CADASTROS'.center(50))
        print(f'{'-' * 50}\033[m')

        print(f'{'NOME':<10} {'IDADE':>39}')
        print(f'{'_'*20:<15} {'_'*10:>29}')

        for d in data[1]:
            print(f'\033[1;93m{d[0]:<30} \033[1;94m{d[1]:>19}\033[m')

        menuPrincipal()
    else:
        erro(data[1])

def sair():
    print('\033[1;91m-' * 50)
    print('\033[1;91mSAINDO'.center(50))
    print('\033[1;91m-' * 50)


def erro(err):
    print(f'\033[1;91mErro: {err}')


menuPrincipal()
