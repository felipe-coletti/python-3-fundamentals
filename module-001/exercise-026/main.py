sentence = input('Digite uma frase: ').strip().lower()

print(f'A letra A aparece {sentence.count('a')} vezes na frase.')
print(f'A primeira letra A está na posição {sentence.find('a') + 1}.')
print(f'A última letra A está na posição {sentence.rfind('a') + 1}.')
