'''
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
'''

weights = []

for i in range(0, 5):
    weight = float(input(f'Digite o peso da {i + 1} pessoa: '))
    
    weights.append(weight)
    
weights = sorted(weights)

lowerWeight = weights[0]
higherWeight = weights[len(weights) - 1]

print(f'o menor peso é {lowerWeight} Kg e o maior peso é {higherWeight} Kg.')
