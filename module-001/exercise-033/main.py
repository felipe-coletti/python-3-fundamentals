firstNumber = float(input('Digite o primeiro número: '))
secondNumber = float(input('Digite o segundo número: '))
thirdNumber = float(input('Digite o terceiro número: '))

smallerNumber = higherNumber = firstNumber

if secondNumber < smallerNumber:
    smallerNumber = secondNumber
if thirdNumber < smallerNumber:
    smallerNumber = thirdNumber

if secondNumber > higherNumber:
    higherNumber = secondNumber
if thirdNumber > higherNumber:
    higherNumber = thirdNumber

print(f'O menor número é {smallerNumber:.2f} e o maior número é {higherNumber:.2f}.')
