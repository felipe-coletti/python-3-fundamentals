full_name = input('Digite um nome completo: ')

names = full_name.split()

first_name = names[0]
last_name = names[len(names) - 1]

print(f'O primeiro nome é {first_name}.')
print(f'O último nome é {last_name}.')
