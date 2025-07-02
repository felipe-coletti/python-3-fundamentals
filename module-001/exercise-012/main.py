price = float(input('Digite o preço do produto: R$ '))

discounted_price = price - 5 / 100 * price

print(f'O preço do produto, com um desconto de 5%, vai de R$ {price:.2f} para R$ {discounted_price:.2f}.')
