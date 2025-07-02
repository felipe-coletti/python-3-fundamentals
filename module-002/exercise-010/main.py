from random import randint

options = ['Pedra', 'Papel', 'Tesoura']

first_option = int(input('Escolha uma opção:\n[1] Pedra.\n[2] Papel.\n[3] Tesoura.'))

second_option = randint(1, 3)

if 0 < first_option < 4:
    print(f'Jogador 1 escolheu {options[first_option - 1]}.\nJogador 2 escolheu {options[second_option - 1]}.')
    
    if first_option - 1 == second_option or first_option == 1 and second_option == 3:
        print('Você ganhou.')
    elif second_option - 1 == first_option or second_option == 1 and first_option == 3:
        print('Você perdeu.')
    else:
        print('Empate.')
else:
    print('Opção inválida.')
