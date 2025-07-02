decimalNumber = int(input('Digite um número inteiro: '))
option = int(input('Digite:\n1 para converter para um número binário;\n2 para converter para um número octal;\n3 para converter para um número hexadecimal.'))

if option == 1:
    binaryNumber = bin(decimalNumber)[2:]
    
    print(f'O número {decimalNumber} convertido para um número binário é: {binaryNumber}.')
elif option == 2:
    octalNumber = oct(decimalNumber)[2:]
    
    print(f'O número {decimalNumber} convertido para um número octal é: {octalNumber}.')
elif option == 3:
    hexadecimalNumber = hex(decimalNumber)[2:]
    
    print(f'O número {decimalNumber} convertido para um número hexadecimal é: {hexadecimalNumber}.')
else:
    print('Número inválido.')
