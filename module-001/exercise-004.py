'''
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
'''

something = input('Digite algo: ')

print(f'O tipo primitivo é: {type(something)}')
print(f'É composto apenas por espaços? {something.isspace()}')
print(f'É composto apenas por números? {something.isnumeric()}')
print(f'É composto apenas por letras? {something.isalpha()}')
print(f'É composto apenas por números e letras? {something.isalnum()}')
print(f'É composto apenas por letras maiúsculas? {something.isupper()}')
print(f'É composto apenas por letras minúsculas? {something.islower()}')
print(f'Está capitalizado? {something.istitle()}')
