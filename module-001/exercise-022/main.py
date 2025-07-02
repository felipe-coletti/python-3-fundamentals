full_name = input('Digite um nome completo: ')

names = full_name.split()

first_name = names[0]

print(f'O nome em letras maiúsculas é {full_name.upper()}.')
print(f'O nome em letras minúsculas é {full_name.lower()}.')
print(f'O nome tem {len(full_name.replace(' ', ''))} letras.')
print(f'O primeiro nome é {first_name} e ele tem {len(first_name)} letras.')
