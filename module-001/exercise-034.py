'''
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$ 1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
'''

salary = float(input('Digite o salário de um funcionário: R$ '))

if salary > 1250:
    increase = 10
    newSalary = salary + increase / 100 * salary
else:
    increase = 15
    newSalary = salary + increase / 100 * salary

print('O salário do funcionário, com um aumento de {}%, vai de R$ {:.2f} para R$ {:.2f}.'.format(increase, salary, newSalary))
