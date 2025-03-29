'''
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
'''

salary = float(input('Digite o salário de um funcionário: R$ '))

newSalary = salary + 15 / 100 * salary

print(f'O salário do funcionário, com um aumento de 15%, vai de R$ {salary:.2f} para R$ {newSalary:.2f}.')
