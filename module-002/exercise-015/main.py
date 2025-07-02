sum = 0

for i in range(0, 6):
    number = int(input('Digite um número inteiro: '))
    
    if number % 2 == 0:
        sum += number

print(f'A soma dos números pares digitados é {sum}.')
