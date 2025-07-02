house_price = float(input('Digite o preço da casa: R$ '))
salary = float(input('Digite o salário do comprador: R$ '))
years = int(input('Digite em quantos anos o comprador pretende pagar a casa: '))

months = years * 12

installment = house_price / months

installmentLimit = 30 / 100 * salary

if installment <= installmentLimit:
    print(f'O empréstimo foi aprovado. A prestação será de R$ {installment:.2f} por mês.')
else:
    print('O empréstimo foi negado. A prestação excederia 30% do salário do comprador.')
