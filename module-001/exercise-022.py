'''
Crie um programa que leia o nome completo de uma pessoa e mostre: o nome com todas as letras maiúsculas e minúsculas, quantas letras ao todo (sem considerar espaços) e quantas letras tem o primeiro nome.
'''

fullName = input('Digite um nome completo: ')

names = fullName.split()

firstName = names[0]

print(f'O nome em letras maiúsculas é {fullName.upper()}.')
print(f'O nome em letras minúsculas é {fullName.lower()}.')
print(f'O nome tem {len(fullName.replace(' ', ''))} letras.')
print(f'O primeiro nome é {firstName} e ele tem {len(firstName)} letras.')
