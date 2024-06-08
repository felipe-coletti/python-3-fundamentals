'''
Crie um programa que leia um número real qualquer pelo teclado e mostra na tela a sua porção inteira.
'''

from math import trunc

number = float(input('Digite um número: '))

print('A parte inteira de {:.2f} é {}.'.format(number, trunc(number)))
