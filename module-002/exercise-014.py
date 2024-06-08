'''
Refaça o desafio 9 do 1º módulo, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
'''

number = int(input('Digite um número inteiro: '))

for i in range(1, 11):
    print('{} x {} = {}'.format(number, i, number * i))
