price = float(input('Digite o preço da compra: R$ '))

payment_method = int(input('Formas de pagamento:\n[1] à vista no dinheiro/cheque.\n[2] à vista no cartão.\n[3] 2x no cartão.\n[4] 3x ou mais no cartão.\nSelecione uma opção.'))

if payment_method == 1:
    print('10% de desconto.')
    
    total_price = 90 / 100 * price
elif payment_method == 2:
    print('5% de desconto.')
    
    total_price = 95 / 100 * price
elif payment_method == 3:
    print('Preço normal.')
    
    total_price = price
    
    print(f'Valor da parcela: R$ {total_price / 2:.2f}.')
elif payment_method == 4:
    instalments_number = int(input('Digite o número de parcelas: '))
    
    print('20% de juros mensais.')
    
    total_price = price + 20 / 100 * price
    instalment = total_price / instalments_number
    
    print(f'Valor da parcela: R$ {instalment:.2f}.')
else:
    print('Opção inválida.')

print(f'Total a pagar: R${total_price:.2f}.')
