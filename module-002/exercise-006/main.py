from datetime import date

birth_year = int(input('Digite o ano de nascimento: '))

current_year = date.today().year

if birth_year <= current_year:
    years_old = current_year - birth_year
    
    if years_old > 25:
        category = 'Master'
    elif years_old >= 20:
        category = 'Sénior'
    elif years_old >= 15:
        category = 'Júnior'
    elif years_old >= 10:
        category = 'Infantil'
    else:
        category = 'Mirim'
        
    print(f'A categoria é: {category}.')
else:
    print('Ano de nascimento inválido.')
