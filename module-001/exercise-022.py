'''
Crie um programa que leia o nome completo de uma pessoa e mostre: o nome com todas as letras maiúsculas e minúsculas, quantas letras ao todo (sem considerar espaços) e quantas letras tem o primeiro nome.
'''

fullName = input('Digite um nome completo: ')

names = fullName.split()

firstName = names[0]

print('O nome em letras maiúsculas é {}.'.format(fullName.upper()))
print('O nome em letras minúsculas é {}.'.format(fullName.lower()))
print('O nome tem {} letras.'.format(len(fullName.replace(' ', ''))))
print('O primeiro nome é {} e ele tem {} letras.'.format(firstName, len(firstName)))
