'''
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
'''

phrase = str(input('Digite uma frase: ')).strip().replace(' ', '').upper()

invertedPhrase = phrase[::-1]

print('O contrário de {} é {}.'.format(phrase, invertedPhrase))

if phrase == invertedPhrase:
    print('A frase é um palíndromo.')
else:
    print('A frase não é um palíndromo.')