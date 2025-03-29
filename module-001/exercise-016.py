'''
Crie um programa que leia um número real qualquer pelo teclado e mostra na tela a sua porção inteira.
'''

from math import trunc

number = float(input('Digite um número: '))

print(f'A parte inteira de {number:.2f} é {trunc(number)}.')
