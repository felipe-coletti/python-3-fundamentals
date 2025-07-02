km = float(input('Digite quantos quilômetros foram percorridos com o carro: '))
days = int(input('Digite por quantos dias o carro foi alugado: '))

price = 0.15 * km + 60 * days

print(f'O preço total a pagar é de R$ {price:.2f}.')
