def boletim(*notas, sit=False):
    '''
    Essa função lê as notas passadas dos alunos e retorna seu boletim em forma de array.
    :param notas: Notas dos alunos
    :param sit: Mostrar situação: Aprovado | Reprovado
    :return: Um array do boletim
    '''
    boletim = {
        'qtdNotas': len(notas),
        'maiorNota': max(notas),
        'menorNota': min(notas),
        'media': sum(notas) / len(notas),
    }

    if sit:
        if boletim['media'] < 60:
            boletim['situação'] = 'Reprovado'
        else:
            boletim['situação'] = 'Aprovado'

    return boletim

help(boletim)
print(boletim(20, 50, 60, 70, 40, 50, sit=True))