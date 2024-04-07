def cadastrar(n, i):
    try:
        with open('data/dados.txt', 'a') as arquivo:
            arquivo.write(f'{n}, {i}\n')
            return ['sucesso']

    except:
        return ['erro', '401']


def listar():
    try:
        data = []

        with open('data/dados.txt', 'r') as arquivo:
            for linha in arquivo:
                data.append(linha.split(', '))

            for d in data:
                d[1] = d[1].replace(f'{d[1][-1]}', '')

            return ['sucesso', data]

    except:
        return ['erro', '402']
