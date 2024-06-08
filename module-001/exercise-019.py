'''
Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele lendo os nomes deles e escrevendo o nome do escolhido.
'''

from random import choice

firstStudent = input('Digite o nome do primeiro aluno: ')
secondStudent = input('Digite o nome do segundo aluno: ')
thirdStudent = input('Digite o nome do terceiro aluno: ')
fourthStudent = input('Digite o nome do quarto aluno: ')

students = [firstStudent, secondStudent, thirdStudent, fourthStudent]

print('O aluno sorteado foi {}.'.format(choice(students)))
