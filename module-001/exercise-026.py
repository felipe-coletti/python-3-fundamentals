'''
Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
'''

sentence = input('Digite uma frase: ').strip().lower()

print(f'A letra A aparece {sentence.count('a')} vezes na frase.')
print(f'A primeira letra A está na posição {sentence.find('a') + 1}.')
print(f'A última letra A está na posição {sentence.rfind('a') + 1}.')
