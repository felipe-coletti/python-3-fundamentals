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
        print('O alistamento foi a {} ano.'.format(lagTime))
    else:
        print('O alistamento foi a {} anos.'.format(lagTime))
elif yearsOld == 18:
    print('O alistamento é esse ano.')
else:
    timeLeft = 18 - yearsOld
    
    if timeLeft == 1:
        print('Falta {} ano para o alistamento.'.format(timeLeft))
    else:
        print('Faltam {} anos para o alistamento.'.format(timeLeft))
