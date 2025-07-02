from random import randint

typedNumber = int(input('Digite um número inteiro entre 0 e 5: '))

drawnNumber = randint(0, 5)

if typedNumber == drawnNumber:
    print(f'Você acertou, o número sorteado foi {drawnNumber}.')
else:
    print(f'Você errou, o número sorteado foi {drawnNumber}.')
