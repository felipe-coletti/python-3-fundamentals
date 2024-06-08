'''
Escreva um programa que pergunta a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por Km rodado.
'''

km = float(input('Digite quantos quilômetros foram percorridos com o carro: '))
days = int(input('Digite por quantos dias o carro foi alugado: '))

price = 0.15 * km + 60 * days

print('O preço total a pagar é de R$ {:.2f}.'.format(price))
