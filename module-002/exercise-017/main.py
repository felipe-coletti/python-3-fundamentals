number = int(input('Digite um número: '))

if number < 0:
    print('Não existem números primos negativos.')
elif number == 0:
    print('O número 0 não é um número primo porque pode ser dividido por qualquer número que não seja ele mesmo.')
elif number == 1:
    print('O número 1 não é um número primo porque só pode ser dividido por ele mesmo.')
else:
    divisors_number = 0
    number_divisors = ''
    
    for i in range(1, number + 1):
        if number % i == 0:
            if i < number:
                if divisors_number > 0:
                    number_divisors += ', '
                
                number_divisors += str(i)
            else:
                number_divisors += f' e {i}'
            
            divisors_number += 1
        
    if divisors_number == 2:
        print(f'O número {number} é um número primo por que só pode ser dividido por 1 e por ele mesmo.')
    else:
        print(f'O número {number} não é um número primo porque pode ser dividido por {number_divisors}.')
