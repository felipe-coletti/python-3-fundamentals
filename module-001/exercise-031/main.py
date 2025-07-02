distance = int(input('Digite a distância da viagem em quilometros: '))

if distance <= 200:
    ticket_price = distance * 0.50
else: 
    ticket_price = distance * 0.45
    
print(f'O preço da passagem é R$ {ticket_price:.2f}')
