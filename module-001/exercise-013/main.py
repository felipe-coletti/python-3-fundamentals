salary = float(input('Digite o salário de um funcionário: R$ '))

new_salary = salary + 15 / 100 * salary

print(f'O salário do funcionário, com um aumento de 15%, vai de R$ {salary:.2f} para R$ {new_salary:.2f}.')
