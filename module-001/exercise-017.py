'''
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
'''

from math import sqrt

a = float(input('Digite o valor do cateto oposto: '))
b = float(input('Digite o valor do cateto adjacente: '))

c = sqrt(a**2 + b**2)

print('O valor da hipotenusa é {:.2f}.'.format(c))
