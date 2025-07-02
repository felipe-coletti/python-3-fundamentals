from random import shuffle

firstStudent = input('Digite o nome do primeiro aluno: ')
secondStudent = input('Digite o nome do segundo aluno: ')
thirdStudent = input('Digite o nome do terceiro aluno: ')
fourthStudent = input('Digite o nome do quarto aluno: ')

students = [firstStudent, secondStudent, thirdStudent, fourthStudent]

shuffle(students)

print(f'A ordem de apresentação dos trabalhos é {students[0]}, {students[1]}, {students[2]} e {students[3]}.')
