'''
Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
'''

sum = 0

for i in range(1, 501):
    if i % 2 != 0 and i % 3 == 0:
        sum += i
        
print(f'A soma dos números impares múltiplos de 3 entre 1 e 500 é: {sum}.')
