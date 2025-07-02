year = input('Digite um ano: ')

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f'{year} é um ano bissexto.')
else:
    print(f'{year} não é um ano bissexto.')
