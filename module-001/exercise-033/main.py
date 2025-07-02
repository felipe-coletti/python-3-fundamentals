first_number = float(input('Digite o primeiro número: '))
second_number = float(input('Digite o segundo número: '))
third_number = float(input('Digite o terceiro número: '))

smaller_number = higher_number = first_number

if second_number < smaller_number:
    smaller_number = second_number
if third_number < smaller_number:
    smaller_number = third_number

if second_number > higher_number:
    higher_number = second_number
if third_number > higher_number:
    higher_number = third_number

print(f'O menor número é {smaller_number:.2f} e o maior número é {higher_number:.2f}.')
