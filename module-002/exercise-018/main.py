phrase = input('Digite uma frase: ').strip().replace(' ', '').upper()

invertedPhrase = phrase[::-1]

print(f'O contrário de {phrase} é {invertedPhrase}.')

if phrase == invertedPhrase:
    print('A frase é um palíndromo.')
else:
    print('A frase não é um palíndromo.')
