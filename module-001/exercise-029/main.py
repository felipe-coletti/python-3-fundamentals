speed = int(input('Digite a velocidade do veículo em quilometros por hora: '))

if speed <= 80:
    print('O veículo está dentro do limite de velocidade.')
else:
    speedOverLimit = speed - 80
    finePrice = speedOverLimit * 7
    
    print(f'O veículo está {speedOverLimit} Km/h acima do limite de velocidade e será multado em R$ {finePrice:.2f}.')
