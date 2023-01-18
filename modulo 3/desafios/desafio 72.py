numExtenso = ('zero' , 'um' , 'dois' , 'três' , 'quatro' , 'cinco' , 'seis' , 'sete' , 'oito' , 'nove' , 'dez')

while True:
    num = int(input('Digite um número de 1 até 10: '))
    if num > 10:
        break
    else:
        print(numExtenso[num])