from random import shuffle

first_student = input('Digite o nome do primeiro aluno: ')
second_student = input('Digite o nome do segundo aluno: ')
third_student = input('Digite o nome do terceiro aluno: ')
fourth_student = input('Digite o nome do quarto aluno: ')

students = [first_student, second_student, third_student, fourth_student]

shuffle(students)

print(f'A ordem de apresentação dos trabalhos é {students[0]}, {students[1]}, {students[2]} e {students[3]}.')
