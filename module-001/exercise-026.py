'''
Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
'''

sentence = input('Digite uma frase: ').strip().lower()

print('A letra A aparece {} vezes na frase.'.format(sentence.count('a')))
print('A primeira letra A está na posição {}.'.format(sentence.find('a') + 1))
print('A última letra A está na posição {}.'.format(sentence.rfind('a') + 1))
