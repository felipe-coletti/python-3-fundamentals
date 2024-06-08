'''
Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
'''

number = int(input('Digite um número: '))

predecessor = number - 1
successor = number + 1

print('O antecessor de {} é {}.'.format(number, predecessor))
print('O sucessor de {} é {}.'.format(number, successor))
