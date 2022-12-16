'''
Ana gosta muito de matemática e de brincar com números. Ela definiu o conceito de "Número da Ana. Se um número inteiro não negativo N é produto de três números inteiros consecutivos então N é um "Número da Ana".

Faça um programa que leia um número inteiro não negativo N e imprima "S" se for um "Número da Ana" e "N" caso contrário. Por exemplo, 120 é um "Número da Ana", pois é resultado da multiplicação 4 x 5 x 6.
'''
n = int(input())
x = 1
numero_ana = 1
while numero_ana < n:
    numero_ana = numero_ana * (x)
    x = x + 1
if numero_ana == n:
    print("S")
else:
    print("N")
    
    
    

    
