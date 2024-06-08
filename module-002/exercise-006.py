'''
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: mirim;
- De 10 a 14 anos: infantil;
- De 15 a 19 anos: júnior;
- De 20 a 25 anos: sênior;
- Acima de 25 anos: master.
'''

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
        
    print('A categoria é: {}.'.format(category))
else:
    print('Ano de nascimento inválido.')
