'''
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
'''

number = int(input('Digite um número inteiro: '))

thousandUnit = number // 1000
hundred = number // 100 % 10
ten = number // 10 % 10
unit = number // 1 % 10

print('O número {} possui:\n{} UM\n{} C\n{} D\n{} U'.format(number, thousandUnit, hundred, ten, unit))
