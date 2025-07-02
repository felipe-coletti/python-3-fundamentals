speed = int(input('Digite a velocidade do veículo em quilometros por hora: '))

if speed <= 80:
    print('O veículo está dentro do limite de velocidade.')
else:
    speed_over_limit = speed - 80
    fine_price = speed_over_limit * 7
    
    print(f'O veículo está {speed_over_limit} Km/h acima do limite de velocidade e será multado em R$ {fine_price:.2f}.')
