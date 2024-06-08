'''
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80 Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$ 7,00 por cada Km acima do limite.
'''

speed = int(input('Digite a velocidade do veículo em quilometros por hora: '))

if speed <= 80:
    print('O veículo está dentro do limite de velocidade.')
else:
    speedOverLimit = speed - 80
    finePrice = speedOverLimit * 7
    
    print('O veículo está {} Km/h acima do limite de velocidade e será multado em R$ {:.2f}.'.format(speedOverLimit, finePrice))
