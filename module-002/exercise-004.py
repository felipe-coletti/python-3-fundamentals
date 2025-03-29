'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''

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
