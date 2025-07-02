price = float(input('Digite o preço do produto: R$ '))

discountedPrice = price - 5 / 100 * price

print(f'O preço do produto, com um desconto de 5%, vai de R$ {price:.2f} para R$ {discountedPrice:.2f}.')
