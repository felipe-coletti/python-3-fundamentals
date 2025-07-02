from random import choice

first_student = input('Digite o nome do primeiro aluno: ')
second_student = input('Digite o nome do segundo aluno: ')
third_student = input('Digite o nome do terceiro aluno: ')
fourth_student = input('Digite o nome do quarto aluno: ')

students = [first_student, second_student, third_student, fourth_student]

print(f'O aluno sorteado foi {choice(students)}.')
