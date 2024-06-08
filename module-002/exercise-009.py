'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros
'''

price = float(input('Digite o preço da compra: R$ '))

paymentMethod = int(input('Formas de pagamento:\n[1] à vista no dinheiro/cheque.\n[2] à vista no cartão.\n[3] 2x no cartão.\n[4] 3x ou mais no cartão.\nSelecione uma opção.'))

if paymentMethod == 1:
    print('10% de desconto.')
    
    totalPrice = 90 / 100 * price
elif paymentMethod == 2:
    print('5% de desconto.')
    
    totalPrice = 95 / 100 * price
elif paymentMethod == 3:
    print('Preço normal.')
    
    totalPrice = price
    
    print('Valor da parcela: R$ {:.2f}.'.format(totalPrice / 2))
elif paymentMethod == 4:
    instalmentsNumber = int(input('Digite o número de parcelas: '))
    
    print('20% de juros mensais.')
    
    totalPrice = price + 20 / 100 * price
    instalment = totalPrice / instalmentsNumber
    
    print('Valor da parcela: R$ {:.2f}.'.format(instalment))
else:
    print('Opção inválida.')

print('Total a pagar: R${:.2f}.'.format(totalPrice))
