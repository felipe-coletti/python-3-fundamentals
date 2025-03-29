'''
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
'''

fullName = input('Digite um nome completo: ')

names = fullName.split()

firstName = names[0]
lastName = names[len(names) - 1]

print(f'O primeiro nome é {firstName}.')
print(f'O último nome é {lastName}.')
