'''
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
'''

from math import radians, sin, cos, tan

angle = float(input('Digite o valor de um ângulo: '))

sin = sin(radians(angle))
cos = cos(radians(angle))
tan = tan(radians(angle))

print(f'O seno de {angle:.2f} é {sin:.2f}.')
print(f'O cosseno de {angle:.2f} é {cos:.2f}.')
print(f'A tangente de {angle:.2f} é {tan:.2f}.')
