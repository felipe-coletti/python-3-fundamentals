'''
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
'''

a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))

if a < b + c and b < a + c and c < a + b:
    print('Os segmentos de reta a, b e c podem formar um triângulo.')
else:
    print('Os segmentos de reta a, b e c não podem formar um triângulo.')
