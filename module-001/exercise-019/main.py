from random import choice

firstStudent = input('Digite o nome do primeiro aluno: ')
secondStudent = input('Digite o nome do segundo aluno: ')
thirdStudent = input('Digite o nome do terceiro aluno: ')
fourthStudent = input('Digite o nome do quarto aluno: ')

students = [firstStudent, secondStudent, thirdStudent, fourthStudent]

print(f'O aluno sorteado foi {choice(students)}.')
