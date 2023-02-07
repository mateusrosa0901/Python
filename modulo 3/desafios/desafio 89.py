ficha = []
boletim = []
loop = str('')

while True:
    nome = str(input('Digite o nome do aluno(a): '))
    nota1 = float(input('Digite a 1° nota: '))
    nota2 = float(input('Digite a 2° nota: '))
    media = (nota1 + nota2) / 2
    ficha.append(nome, [nota1, nota2], media)
    boletim.append(ficha[:])
    ficha.clear()

