import random

#levantamento da lista
a1 = input('Digite o nome do 1° aluno: ')
a2 = input('Digite o nome do 2° aluno:')
a3 = input('Digite o nome do 3° aluno: ')
a4 = input('Digite o nome do 4° aluno: ')

#lista
al = [a1 , a2 , a3 , a4]


print(f'O/A {random.choice(al)} vai apagar o quadro hoje!')