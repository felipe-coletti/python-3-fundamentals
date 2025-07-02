name = input('Digite o nome de uma cidade: ')

names = name.split()

first_name = names[0]

print(f'O nome da cidade começa com Santo? {first_name.lower() == 'santo'}')
