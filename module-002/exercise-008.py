'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: abaixo do peso;
- De 18,5 a 24,9: peso ideal;
- De 25 a 29,9: sobrepeso;
- De 30 a 40: obesidade;
- Acima de 40: obesidade mórbida.
'''

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
