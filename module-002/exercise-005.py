'''
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5,0: reprovado;
- Média entre 5,0 e 6,9: recuperação;
- Média 7,0 ou superior: aprovado.
'''

firstGrade = float(input('Digite a primeira nota: '))
secondGrade = float(input('Digite a segunda nota: '))

average = (firstGrade + secondGrade) / 2

print(f'A média é {average:.2f}.')

if average >= 7:
    print('O aluno foi aprovado.')
elif average >= 5:
    print('O aluno terá que fazer uma prova de recuperação.')
else:
    print('O aluno foi reprovado.')

