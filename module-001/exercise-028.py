'''
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''

from random import randint

typedNumber = int(input('Digite um número inteiro entre 0 e 5: '))

drawnNumber = randint(0, 5)

if typedNumber == drawnNumber:
    print(f'Você acertou, o número sorteado foi {drawnNumber}.')
else:
    print(f'Você errou, o número sorteado foi {drawnNumber}.')
