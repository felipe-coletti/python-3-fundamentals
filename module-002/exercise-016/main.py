a1 = float(input('Digite o primeiro termo da progressão aritmética: '))
r = float(input('Digite a razão da progressão aritmética: '))

a = a1

print(a)

while a < a1 + r * 9:
    a += r
    
    print(a)
    
