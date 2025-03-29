'''
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
'''

from datetime import date

currentYear = date.today().year

major = 0
minor = 0

for i in range(0, 7):
    birthYear = int(input(f'Digite o ano de nascimento da {i + 1}ª pessoa: '))
    
    if currentYear - birthYear >= 18:
        major += 1
    else:
        minor += 1
        
print(f'{major} pessoas são maiores de idade e {minor} são menores de idade.')
