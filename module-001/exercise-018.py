'''
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
'''

from math import radians, sin, cos, tan

angle = float(input('Digite o valor de um ângulo: '))

sin = sin(radians(angle))
cos = cos(radians(angle))
tan = tan(radians(angle))

print('O seno de {:.2f} é {:.2f}.'.format(angle, sin))
print('O cosseno de {:.2f} é {:.2f}.'.format(angle, cos))
print('A tangente de {:.2f} é {:.2f}.'.format(angle, tan))
