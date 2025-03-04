'''
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
'''

from datetime import date

currentYear = date.today().year

groups = {
    'major': 0,
    'minor': 0
}

for i in range(0, 7):
    birthYear = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(i + 1)))
    
    if currentYear - birthYear >= 18:
        groups['major'] += 1
    else:
        groups['minor'] += 1
        
print('{} pessoas são maiores de idade e {} são menores de idade.'.format(groups['major'], groups['minor']))
