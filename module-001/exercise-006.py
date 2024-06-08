'''
Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
'''

number = float(input('Digite um número: '))

double = number * 2
triple = number * 3
squareRoot = number**(1/2)

print('O dobro de {:.2f} é {:.2f}.'.format(number, double))
print('O triplo de {:.2f} é {:.2f}.'.format(number, triple))
print('A raiz quadrada de {:.2f} é {:.2f}.'.format(number, squareRoot))
