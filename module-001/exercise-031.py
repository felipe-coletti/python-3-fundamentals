'''
Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens de até 200 Km e R$ 0,45 para viagens mais longas.
'''

distance = int(input('Digite a distância da viagem em quilometros: '))

if distance <= 200:
    ticketPrice = distance * 0.50
else: 
    ticketPrice = distance * 0.45
    
print('O preço da passagem é R$ {:.2f}'.format(ticketPrice))
