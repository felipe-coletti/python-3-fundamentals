from datetime import date

current_year = date.today().year

major = 0
minor = 0

for i in range(0, 7):
    birth_year = int(input(f'Digite o ano de nascimento da {i + 1}ª pessoa: '))
    
    if current_year - birth_year >= 18:
        major += 1
    else:
        minor += 1
        
print(f'{major} pessoas são maiores de idade e {minor} são menores de idade.')
