'''
Escreva um programa que leia um valor em metros e converta para centímetros e milímetros.
'''

m = float(input('Digite um valor em metros: '))

km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000

print(f'{m:.2f} m equivale a:\n{km:.2f} km\n{hm:.2f} hm\n{dam:.2f} dam\n{dm:.2f} dm\n{cm:.2f} cm\n{mm:.2f} mm')
