'''
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
'''

a1 = float(input('Digite o primeiro termo da progressão aritmética: '))
r = float(input('Digite a razão da progressão aritmética: '))

a = a1

print(a)

while a < a1 + r * 9:
    a += r
    
    print(a)
    
