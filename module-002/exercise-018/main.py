phrase = input('Digite uma frase: ').strip().replace(' ', '').upper()

inverted_phrase = phrase[::-1]

print(f'O contrário de {phrase} é {inverted_phrase}.')

if phrase == inverted_phrase:
    print('A frase é um palíndromo.')
else:
    print('A frase não é um palíndromo.')
