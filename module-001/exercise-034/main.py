salary = float(input('Digite o salário de um funcionário: R$ '))

if salary > 1250:
    increase = 10
    newSalary = salary + increase / 100 * salary
else:
    increase = 15
    newSalary = salary + increase / 100 * salary

print(f'O salário do funcionário, com um aumento de {increase}%, vai de R$ {salary:.2f} para R$ {newSalary:.2f}.')
