'''
Considere que seu computador só consegue realizar operações de soma ou subtração, ou seja, está com as operações de divisão e multiplicação inoperantes. Faça um programa que leia dois números inteiros positivos A e B, onde A é a base e B é o expoente de uma potência. Após isso, calcule o valor da potência sem utilizar as operações inoperantes. Imprima o valor de A elevado a B.

Obs: Não utilize bibliotecas matemáticas. No caso de python, não é permitido usar o operador **. Faça sua solução utilizando laço de repetição.
'''
base = int(input())
expoente = int(input())

if base == 0:
    resultado = 0

elif base == 1 or expoente == 1:
    resultado = base

elif expoente == 0:
    resultado = 1

else:
    for i in range(0, expoente-1):
        if i == 0:
            somatoria = base
            resultado = base
        else:
            somatoria = resultado
        for i in range(0, base-1):
            resultado += somatoria


print(resultado)

    


