'''
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
'''

sum = 0

for i in range(0, 6):
    number = int(input('Digite um número inteiro: '))
    
    if number % 2 == 0:
        sum += number

print('A soma dos números pares digitados é {}.'.format(sum))
