'''
Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
'''

firstGrade = float(input('Digite a primeira nota: '))
secondGrade = float(input('Digite a segunda nota: '))

average = (firstGrade + secondGrade) / 2

print('A média entre {:.2f} e {:.2f} é igual a {:.2f}.'.format(firstGrade, secondGrade, average))
