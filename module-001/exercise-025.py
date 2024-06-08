'''
Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.
'''

fullName = input('Digite um nome completo: ')

print('O nome tem Silva? {}'.format('silva' in fullName.lower()))
