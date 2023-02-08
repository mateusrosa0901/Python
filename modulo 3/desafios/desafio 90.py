ficha = {}

ficha['nome'] = str(input('Digite o nome do aluno: '))
ficha['media'] = float(input('Digite a média do aluno: '))

if ficha['media'] >= 7:
    ficha['situacao'] = 'APROVADO'

else:
    ficha['media'] = 'REPROVADO'

print(f'nome | média | situação')
print(f'{ficha["nome"]} | {ficha["media"]:.1f} | {ficha["situacao"]}')
