from datetime import date

birthYear = int(input('Digite o ano de nascimento: '))

currentYear = date.today().year

if birthYear <= currentYear:
    yearsOld = currentYear - birthYear
    
    if yearsOld > 25:
        category = 'Master'
    elif yearsOld >= 20:
        category = 'Sénior'
    elif yearsOld >= 15:
        category = 'Júnior'
    elif yearsOld >= 10:
        category = 'Infantil'
    else:
        category = 'Mirim'
        
    print(f'A categoria é: {category}.')
else:
    print('Ano de nascimento inválido.')
