from random import randint

typed_number = int(input('Digite um número inteiro entre 0 e 5: '))

drawn_number = randint(0, 5)

if typed_number == drawn_number:
    print(f'Você acertou, o número sorteado foi {drawn_number}.')
else:
    print(f'Você errou, o número sorteado foi {drawn_number}.')
