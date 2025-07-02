fullName = input('Digite um nome completo: ')

names = fullName.split()

firstName = names[0]
lastName = names[len(names) - 1]

print(f'O primeiro nome é {firstName}.')
print(f'O último nome é {lastName}.')
