vcasa = float(input('Valor da casa: R$'))
salario = float(input('Valor do salário: R$'))
tempo = int(input('Anos parcelado: '))

mes = tempo * 12
vmensal = vcasa / mes
porsalario = salario * 0.3

if vmensal > porsalario:
    print('\033[31mEmpéstimo negado\033')

else:
    print('\033[32mEmpéstimo aceito\033')