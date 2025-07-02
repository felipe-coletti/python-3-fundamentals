fullName = input('Digite um nome completo: ')

names = fullName.split()

firstName = names[0]

print(f'O nome em letras maiúsculas é {fullName.upper()}.')
print(f'O nome em letras minúsculas é {fullName.lower()}.')
print(f'O nome tem {len(fullName.replace(' ', ''))} letras.')
print(f'O primeiro nome é {firstName} e ele tem {len(firstName)} letras.')
