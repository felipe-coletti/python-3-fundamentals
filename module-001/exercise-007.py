'''
Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
'''

firstGrade = float(input('Digite a primeira nota: '))
secondGrade = float(input('Digite a segunda nota: '))

average = (firstGrade + secondGrade) / 2

print(f'A média entre {firstGrade:.2f} e {secondGrade:.2f} é igual a {average:.2f}.')
