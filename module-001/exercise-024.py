'''
Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "Santo".
'''

name = input('Digite o nome de uma cidade: ')

nameParts = name.split()

nameFirstPart = nameParts[0]

print(f'O nome da cidade começa com Santo? {nameFirstPart.lower() == 'santo'}')
