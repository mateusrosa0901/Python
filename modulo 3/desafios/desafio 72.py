numExtenso = ('zero' , 'um' , 'dois' , 'três' , 'quatro' , 'cinco' , 'seis' , 'sete' , 'oito' , 'nove' , 'dez')

while True:
    print('-'*20)
    num = int(input('Digite um número de 0 até 10: '))
    if num > 10 or num < 0:
        break
    else:
        print(numExtenso[num])