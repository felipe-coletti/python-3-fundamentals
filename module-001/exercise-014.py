'''
Escreva um programa que leia uma temperatura em graus Celsius e converta para graus Fahrenheit.
'''

c = float(input('Digite uma temperatura em °C: '))

f = (c * 9 / 5) + 32
k = c + 273.15

print('{:.2f} °C equivale a {:.2f} °F e {:.2f} °K.'.format(c, f, k))
