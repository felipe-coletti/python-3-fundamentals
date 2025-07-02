from datetime import date

birth_year = int(input('Digite o ano de nascimento: '))

current_year = date.today().year

years_old = current_year - birth_year
    
if years_old > 18:
    lag_time = years_old - 18
    
    if lag_time == 1:
        print(f'O alistamento foi a {lag_time} ano.')
    else:
        print(f'O alistamento foi a {lag_time} anos.')
elif years_old == 18:
    print('O alistamento é esse ano.')
else:
    time_left = 18 - years_old
    
    if time_left == 1:
        print(f'Falta {time_left} ano para o alistamento.')
    else:
        print(f'Faltam {time_left} anos para o alistamento.')
