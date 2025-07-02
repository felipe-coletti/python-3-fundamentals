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

