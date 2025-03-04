'''
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
'''

weights = []

for i in range(0, 5):
    weight = float(input('Digite o peso da {} pessoa: '.format(i + 1)))
    
    weights.append(weight)
    
weights = sorted(weights)

print('o maior peso é {} Kg e o menor peso é {} Kg.'.format(weights[len(weights) - 1], weights[0]))
