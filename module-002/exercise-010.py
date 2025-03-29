'''
Crie um programa que faça o computador jogar Jokenpô com você.
'''

from random import randint

options = ['Pedra', 'Papel', 'Tesoura']

firstOption = int(input('Escolha uma opção:\n[1] Pedra.\n[2] Papel.\n[3] Tesoura.'))

secondOption = randint(1, 3)

if 0 < firstOption < 4:
    print(f'Jogador 1 escolheu {options[firstOption - 1]}.\nJogador 2 escolheu {options[secondOption - 1]}.')
    
    if firstOption - 1 == secondOption or firstOption == 1 and secondOption == 3:
        print('Você ganhou.')
    elif secondOption - 1 == firstOption or secondOption == 1 and firstOption == 3:
        print('Você perdeu.')
    else:
        print('Empate.')
else:
    print('Opção inválida.')
