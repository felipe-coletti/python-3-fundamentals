from datetime import date

birthYear = int(input('Digite o ano de nascimento: '))

currentYear = date.today().year

yearsOld = currentYear - birthYear
    
if yearsOld > 18:
    lagTime = yearsOld - 18
    
    if lagTime == 1:
        print(f'O alistamento foi a {lagTime} ano.')
    else:
        print(f'O alistamento foi a {lagTime} anos.')
elif yearsOld == 18:
    print('O alistamento é esse ano.')
else:
    timeLeft = 18 - yearsOld
    
    if timeLeft == 1:
        print(f'Falta {timeLeft} ano para o alistamento.')
    else:
        print(f'Faltam {timeLeft} anos para o alistamento.')
