'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
'''

housePrice = float(input('Digite o preço da casa: R$ '))
salary = float(input('Digite o salário do comprador: R$ '))
years = int(input('Digite em quantos anos o comprador pretende pagar a casa: '))

months = years * 12

installment = housePrice / months

installmentLimit = 30 / 100 * salary

if installment <= installmentLimit:
    print('O empréstimo foi aprovado. A prestação será de R$ {:.2f} por mês.'.format(installment))
else:
    print('O empréstimo foi negado. A prestação excederia 30% do salário do comprador.')
