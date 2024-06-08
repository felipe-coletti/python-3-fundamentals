'''
O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
'''

from random import shuffle

firstStudent = input('Digite o nome do primeiro aluno: ')
secondStudent = input('Digite o nome do segundo aluno: ')
thirdStudent = input('Digite o nome do terceiro aluno: ')
fourthStudent = input('Digite o nome do quarto aluno: ')

students = [firstStudent, secondStudent, thirdStudent, fourthStudent]

shuffle(students)

print('A ordem de apresentação dos trabalhos é {}, {}, {} e {}.'.format(students[0], students[1], students[2], students[3]))
