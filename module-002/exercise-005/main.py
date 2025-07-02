first_grade = float(input('Digite a primeira nota: '))
second_grade = float(input('Digite a segunda nota: '))

average = (first_grade + second_grade) / 2

print(f'A média é {average:.2f}.')

if average >= 7:
    print('O aluno foi aprovado.')
elif average >= 5:
    print('O aluno terá que fazer uma prova de recuperação.')
else:
    print('O aluno foi reprovado.')

