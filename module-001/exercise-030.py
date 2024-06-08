'''
Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.
'''

number = int(input('Digite um número inteiro: '))

if number % 2 == 0:
    print('O número {} é par.'.format(number))
else:
    print('O número {} é impar'.format(number))
