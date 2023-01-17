from binascii import a2b_base64
import random

a1 = input('Digite o nome do 1° aluno: ')
a2 = input('Digite o nome do 2° aluno: ')
a3 = input('Digite o nome do 3° aluno: ')
a4 = input('Digite o nome do 4° aluno: ')

al = [a1 , a2 , a3 , a4]
random.shuffle(al)
print('Ordem de apresentação:')
print(al)