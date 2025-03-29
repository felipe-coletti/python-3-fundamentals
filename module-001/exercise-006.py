'''
Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
'''

number = float(input('Digite um número: '))

double = number * 2
triple = number * 3
squareRoot = number**(1/2)

print(f'O dobro de {number:.2f} é {double:.2f}.')
print(f'O triplo de {number:.2f} é {triple:.2f}.')
print(f'A raiz quadrada de {number:.2f} é {squareRoot:.2f}.')
