mass = float(input('Digite o peso: '))
height = float(input('Digite a altura: '))

bmi = mass / height**2

print(f'O IMC é de {bmi:.2f} Kg/m².')

if bmi > 40:
    print('Status: Obesidade mórbida.')
elif bmi >= 30:
    print('Status: Obesidade.')
elif bmi >= 25:
    print('Status: Sobrepeso.')
elif bmi >= 18.5:
    print('Status: Peso ideal.')
else:
    print('Status: Abaixo do peso.')
