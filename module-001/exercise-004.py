'''
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
'''

something = input('Digite algo: ')

print('O tipo primitivo é: {}'.format(type(something)))
print('É composto apenas por espaços? {}'.format(something.isspace()))
print('É composto apenas por números? {}'.format(something.isnumeric()))
print('É composto apenas por letras? {}'.format(something.isalpha()))
print('É composto apenas por números e letras? {}'.format(something.isalnum()))
print('É composto apenas por letras maiúsculas? {}'.format(something.isupper()))
print('É composto apenas por letras minúsculas? {}'.format(something.islower()))
print('Está capitalizado? {}'.format(something.istitle()))
