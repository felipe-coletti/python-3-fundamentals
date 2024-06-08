'''
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
'''

price = float(input('Digite o preço do produto: R$ '))

discountedPrice = price - 5 / 100 * price

print('O preço do produto, com um desconto de 5%, vai de R$ {:.2f} para R$ {:.2f}.'.format(price, discountedPrice))
