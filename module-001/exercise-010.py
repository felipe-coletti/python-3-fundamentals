'''
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere USD$ 1,00 = R$ 3,27.
'''

real = float(input('Digite um valor em reais: '))

dollar = real / 3.27

print(f'R$ {real:.2f} equivale a USD$ {dollar:.2f}.')
