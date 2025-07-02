decimal_number = int(input('Digite um número inteiro: '))
option = int(input('Digite:\n1 para converter para um número binário;\n2 para converter para um número octal;\n3 para converter para um número hexadecimal.'))

if option == 1:
    binary_number = bin(decimal_number)[2:]
    
    print(f'O número {decimal_number} convertido para um número binário é: {binary_number}.')
elif option == 2:
    octal_number = oct(decimal_number)[2:]
    
    print(f'O número {decimal_number} convertido para um número octal é: {octal_number}.')
elif option == 3:
    hexadecimal_number = hex(decimal_number)[2:]
    
    print(f'O número {decimal_number} convertido para um número hexadecimal é: {hexadecimal_number}.')
else:
    print('Número inválido.')
