weights = []

for i in range(0, 5):
    weight = float(input(f'Digite o peso da {i + 1} pessoa: '))
    
    weights.append(weight)
    
weights = sorted(weights)

lower_weight = weights[0]
higher_weight = weights[len(weights) - 1]

print(f'o menor peso é {lower_weight} Kg e o maior peso é {higher_weight} Kg.')
