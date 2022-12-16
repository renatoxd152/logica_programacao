#Faça um programa que leia dois números inteiros X e Y e imprima todos os números de X até Y, seguidos nos números de Y até X. Se X for maior que Y, imprima INVALIDO.
x = int(input())
y = int(input())
aux = x

if x > y:
    print("INVALIDO")
else:
    while x <= y:
        print(x)
        x = x + 1
    while y >= aux:
        print (y)
        y = y - 1
        

        
