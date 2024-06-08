'''
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
'''

decimalNumber = int(input('Digite um número inteiro: '))
option = int(input('Digite:\n1 para converter para um número binário;\n2 para converter para um número octal;\n3 para converter para um número hexadecimal.'))

if option == 1:
    binaryNumber = bin(decimalNumber)[2:]
    
    print('O número {} convertido para um número binário é: {}.'.format(decimalNumber, binaryNumber))
elif option == 2:
    octalNumber = oct(decimalNumber)[2:]
    
    print('O número {} convertido para um número octal é: {}.'.format(decimalNumber, octalNumber))
elif option == 3:
    hexadecimalNumber = hex(decimalNumber)[2:]
    
    print('O número {} convertido para um número hexadecimal é: {}.'.format(decimalNumber, hexadecimalNumber))
else:
    print('Número inválido.')
