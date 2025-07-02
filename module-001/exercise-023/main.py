number = int(input('Digite um número inteiro: '))

thousandUnit = number // 1000
hundred = number // 100 % 10
ten = number // 10 % 10
unit = number // 1 % 10

print(f'O número {number} possui:\n{thousandUnit} UM\n{hundred} C\n{ten} D\n{unit} U')
