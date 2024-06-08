'''
Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "Santo".
'''

name = input('Digite o nome de uma cidade: ')

nameParts = name.split()

nameFirstPart = nameParts[0]

print('O nome da cidade começa com Santo? {}'.format(nameFirstPart.lower() == 'santo'))
