distance = int(input('Digite a distância da viagem em quilometros: '))

if distance <= 200:
    ticketPrice = distance * 0.50
else: 
    ticketPrice = distance * 0.45
    
print(f'O preço da passagem é R$ {ticketPrice:.2f}')
